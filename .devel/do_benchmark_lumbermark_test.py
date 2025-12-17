"""
Copyright (C) 2020-2025, Marek Gagolewski, https://www.gagolewski.com


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
#sys.path.append("/home/gagolews/Python/genieclust/.devel")
sys.setrecursionlimit(100000)


import lumbermark
# import robust_single_linkage
# import treelhouette
import genieclust
import numpy as np
import sklearn.model_selection
import numpy as np
import quitefastmst
import scipy.spatial.distance



def outliers_tmp(mst_w, mst_i, n, cutoff_pct=0.925, cutoff_max_size=50):
    """
    ...
    """
    # make adjacency lists:
    mst_a = [ [] for i in range(n) ]
    for i in range(n-1):
        mst_a[mst_i[i, 0]].append(i)
        mst_a[mst_i[i, 1]].append(i)
    for i in range(n):
        mst_a[i] = np.array(mst_a[i])
    mst_a = np.array(mst_a, dtype="object")


    def visit1(v, e):  # v->w  where mst_e[e,:]={v,w}
        nonlocal mst_i, n, mst_a
        iv = int(mst_i[e, 1] == v)
        w = mst_i[e, 1-iv]
        this_size = 1
        for e2 in mst_a[w]:
            if mst_i[e2, 0] != v and mst_i[e2, 1] != v:
                cur_size = visit1(w, e2)
                this_size += cur_size

        mst_size[e, 1-iv]  = this_size
        mst_size[e, iv]    = n-this_size

        return this_size

    mst_size  = -np.ones((n-1, 2), dtype=int)  # sizes: mst_size[e, 0] is the size of the cluster featuring mst_i[e, 0] that appears when we get rid of an edge e
    v = mst_i[np.argmin(mst_w), 0]  # some starting point
    for e in mst_a[v]:
        visit1(v, e)



    def visit2(v, e):  # v->w  where mst_e[e,:]={v,w}
        nonlocal mst_i, labels, mst_a
        iv = int(mst_i[e, 1] == v)
        w = mst_i[e, 1-iv]
        if labels[w] == 1: return  # already visited
        labels[w] = 1
        for e2 in mst_a[w]:
            if mst_i[e2, 0] != v and mst_i[e2, 1] != v:
                visit2(w, e2)

    cutoff_dist = np.quantile(mst_w, cutoff_pct)
    cut_edge = (np.min(mst_size, axis=1) <= cutoff_max_size) & (mst_w >= cutoff_dist)

    labels = np.repeat(0, n)
    for i in np.flatnonzero(cut_edge):
        j = np.argmax(mst_size[i,:])
        if labels[mst_i[i, 1-j]] == 0:
            visit2(mst_i[i,j], i)

    return labels


def lumbermark_tmp(X, n_clusters, M=0, min_cluster_size=10, min_cluster_factor=0.15, use_realdist=True, outlier_cutoff_pct=1.0, outlier_cutoff_max_size=50):
    n = X.shape[0]
    mst_params = dict(
        mutreach_ties="dcore_min",
        mutreach_leaves="reconnect_dcore_min"
    )

    if M <= 1:
        mst_w, mst_i = quitefastmst.mst_euclid(X, **mst_params)
    else:
        mst_w, mst_i, nn_w, nn_i = quitefastmst.mst_euclid(X, M=M, **mst_params)

    if outlier_cutoff_pct < 1.0:
        # increase cutoff_pct and decrease cutoff_max_size as M increases!
        if use_realdist and M>1:
            mst_i2 = mst_i.copy()
            mst_w2 = np.sqrt(np.sum((X[mst_i2[:,0], :]-X[mst_i2[:,1], :])**2, axis=1))
            _order = np.argsort(mst_w2)
            mst_w2 = mst_w2[_order]
            mst_i2 = mst_i2[_order, :]
            is_outlier = outliers_tmp(mst_w2, mst_i2, n, cutoff_pct=outlier_cutoff_pct, cutoff_max_size=outlier_cutoff_max_size)
        else:
            is_outlier = outliers_tmp(mst_w, mst_i, n, cutoff_pct=outlier_cutoff_pct, cutoff_max_size=outlier_cutoff_max_size)

        skip_edges_bool = np.any(is_outlier[mst_i], axis=1)  # which edges are incident with outliers?
        assert np.sum(skip_edges_bool) == np.sum(is_outlier)
        mst_w2 = mst_w[~skip_edges_bool]
        mst_i2 = mst_i[~skip_edges_bool,:]
        res = lumbermark.internal.lumbermark_from_mst(mst_w2, mst_i2, n, n_clusters=n_clusters, min_cluster_size=min_cluster_size, min_cluster_factor=min_cluster_factor)
        cut_edges = genieclust.internal.translate_skipped_indexes(res["cut_edges"], skip_edges_bool)
        cut_edges_bool = np.zeros(mst_i.shape[0], dtype=bool)
        cut_edges_bool[cut_edges] = True
        labels = genieclust.internal.impute_missing_labels(mst_i, res["labels"], cut_edges_bool)
    else:
        res = lumbermark.internal.lumbermark_from_mst(mst_w, mst_i, n, n_clusters=n_clusters, min_cluster_size=min_cluster_size, min_cluster_factor=min_cluster_factor)
        labels = res["labels"]

    return labels



def do_benchmark_test_lumbermark_tmp(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(    # TODO
        M=[1, 3, 5, 7, 10],
        min_cluster_factor=[0.1, 0.15, 0.2, 0.25],
        use_realdist=[True, False],
        outlier_cutoff_pct=[0.0, 0.25, 0.33, 0.5, 0.67, 0.75, 0.9, 0.925, 1.0],
        outlier_cutoff_max_size=[1, 3, 5, 7, 10, 50],
    ))

    print(" >:", end="", flush=True)
    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)

            if param["M"] <= 1 and not param["use_realdist"]: continue

            if param["outlier_cutoff_pct"] >= 1 and param["outlier_cutoff_max_size"] > 1: continue

            if param["outlier_cutoff_pct"] < 0.5 and param["outlier_cutoff_max_size"] > 10: continue


            # name = "f%g_M%d%s"%(param["min_cluster_factor"], param["M"], param["mutreach_adj_type"])
            name = "f%g_M%d_%r_%r_%r" % (
                param["min_cluster_factor"],
                param["M"],
                param["use_realdist"],
                param["outlier_cutoff_pct"],
                param["outlier_cutoff_max_size"]
            )
            this_param = dict(
                X=X,
                n_clusters=K,
                M=param["M"],
                min_cluster_size=10,
                min_cluster_factor=param["min_cluster_factor"],
                use_realdist=param["use_realdist"],
                outlier_cutoff_pct=param["outlier_cutoff_pct"],
                outlier_cutoff_max_size=param["outlier_cutoff_max_size"],
            )
            try:
                y_pred = lumbermark_tmp(**this_param)
                if max(y_pred) != K-1:
                    y_pred = lumbermark_tmp(
                        **{**this_param, **dict(min_cluster_size=1)}
                    )
                    if max(y_pred) != K-1:
                        stop()

                res[K][f"Lumbermark_{name}"] = y_pred+1    # 0-based -> 1-based!!!
            except Exception as e:
                print("%s: %s (%r)" % (e.__class__.__name__, format(e), repr(param)))


    print(":<", end="", flush=True)
    return res



def do_benchmark_test_lumbermark(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(    # TODO
        M=[0, 1, 2, 3, 5, 7, 10, 15],
        min_cluster_factor=[0.05, 0.1, 0.15, 0.25, 0.33],
        # mutreach_adj_type=["-c", "-d", "+d", "+c"][:1],
        preprocess=["none", "leaves"],
        # min_cluster_size=[10],  # not significant
    ))

    # eps = 0.00000011920928955078125
    print(" >:", end="", flush=True)
    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)
            # if param["mutreach_adj_type"] == "-d":
            #     mutreach_adj = -eps
            # elif param["mutreach_adj_type"] == "+d":
            #     mutreach_adj = +eps
            # elif param["mutreach_adj_type"] == "-c":
            #     mutreach_adj = -1-eps
            # elif param["mutreach_adj_type"] == "+c":
            #     mutreach_adj = +1+eps
            # else: stop("incorrect mutreach_adj")

            # name = "f%g_M%d%s"%(param["min_cluster_factor"], param["M"], param["mutreach_adj_type"])
            name = "f%g_M%d_%r"%(
                param["min_cluster_factor"], param["M"], param["preprocess"]
            )
            try:
                y_pred = lumbermark.Lumbermark(
                    n_clusters=K,
                    postprocess="all",
                    M=param["M"],
                    preprocess=param["preprocess"],
                    min_cluster_factor=param["min_cluster_factor"],
                    # quitefastmst_params=dict()
                ).fit_predict(X)    # TODO
                if max(y_pred) != K-1:
                    y_pred = lumbermark.Lumbermark(
                        n_clusters=K,
                        postprocess="all",
                        min_cluster_size=5,
                        M=param["M"],
                        preprocess=param["preprocess"],
                        min_cluster_factor=param["min_cluster_factor"],
                        # quitefastmst_params=dict(mutreach_adj=-eps)
                    ).fit_predict(X)
                    if max(y_pred) != K-1:
                        y_pred = lumbermark.Lumbermark(
                            n_clusters=K,
                            postprocess="all",
                            # min_cluster_size=5,
                            M=param["M"],
                            preprocess="none",
                            min_cluster_factor=param["min_cluster_factor"],
                            # quitefastmst_params=dict(mutreach_adj=-eps)
                        ).fit_predict(X)
                        if max(y_pred) != K-1:
                            stop()

                res[K][f"Lumbermark_{name}"] = y_pred+1    # 0-based -> 1-based!!!
            except Exception as e:
                print("%s: %s (%r)" % (e.__class__.__name__, format(e), repr(param)))


    print(":<", end="", flush=True)
    return res


# def do_benchmark_test_lumbermark(X, Ks):
#     res = dict()
#     for K in Ks: res[K] = dict()
#
#     param_grid = sklearn.model_selection.ParameterGrid(dict(
#         min_cluster_factor=[0.075, 0.125, 0.25, 0.375, 0.5, 0.75, 1.0],
#         n_neighbors=[3, 5, 7, 10, 15],
#         min_cluster_size=[10], #[1, 5, 10, 15],
#         skip_leaves=[True],  #[True, False],
#         noise_threshold=["uhalf"], #["half", "uhalf", "-1", "0", "1", "2"],
#         noise_postprocess=["tree"], #["tree", "closest"],
#     ))
#
#     print(" >:", end="", flush=True)
#     for K in Ks:
#         print(" ", end="", flush=True)
#         for param in param_grid:
#             print(".", end="", flush=True)
#             name = ",".join(["%r" % v for v in param.values()])
#             try:
#                 try:
#                     res[K][f"Test_Lumbermark_{name}"] = lumbermark.Lumbermark(n_clusters=K, **param).fit_predict(X)+1    # 0-based -> 1-based!!!
#                 except Exception as e:
#                     if param["skip_leaves"]:
#                         param["skip_leaves"] = False  # for sipu/spiral
#                         res[K][f"Test_Lumbermark_{name}"] = lumbermark.Lumbermark(n_clusters=K, **param).fit_predict(X)+1    # 0-based -> 1-based!!!
#                     else:
#                         print("%s: %s" % (e.__class__.__name__, format(e)))
#             except Exception as e:
#                 print("%s: %s" % (e.__class__.__name__, format(e)))
#
#     print(":<", end="", flush=True)
#     return res



# def do_benchmark_test_lumbermark2(X, Ks):
#     res = dict()
#     for K in Ks: res[K] = dict()
#
#     param_grid = sklearn.model_selection.ParameterGrid(dict(
#         gini_threshold=[0.3, 0.5, 0.7, 1.0],
#         n_neighbors=[3, 5, 7, 10, 15],
#         noise_threshold=["uhalf"], #["half", "uhalf", "-1", "0", "1", "2"],
#         noise_postprocess=["tree"], #["tree", "closest"],
#     ))
#
#     print(" >:", end="", flush=True)
#     for K in Ks:
#         print(" ", end="", flush=True)
#         for param in param_grid:
#             print(".", end="", flush=True)
#             name = ",".join(["%r" % v for v in param.values()])
#             try:
#                 try:
#                     res[K][f"Test_Lumbermark2_{name}"] = lumbermark.Lumbermark(n_clusters=K, **param).fit_predict(X)+1    # 0-based -> 1-based!!!
#                 except Exception as e:
#                     if param["skip_leaves"]:
#                         param["skip_leaves"] = False  # for sipu/spiral
#                         res[K][f"Test_Lumbermark2_{name}"] = lumbermark.Lumbermark(n_clusters=K, **param).fit_predict(X)+1    # 0-based -> 1-based!!!
#                     else:
#                         print("%s: %s" % (e.__class__.__name__, format(e)))
#             except Exception as e:
#                 print("%s: %s" % (e.__class__.__name__, format(e)))
#
#     print(":<", end="", flush=True)
#     return res


# def do_benchmark_test_robustsl_treelhouette(X, Ks):
#     res = dict()
#     for K in Ks: res[K] = dict()
#
#     print(" >:", end="", flush=True)
#     for K in Ks:
#         print(" ", end="", flush=True)
#         Ls = [
#             #robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=1, min_cluster_factor=0.25, skip_leaves=False, min_cluster_size=10),
#             #robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=1, min_cluster_factor=0.1, skip_leaves=False, min_cluster_size=15),
#             robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=5, min_cluster_factor=0.25, skip_leaves=True, min_cluster_size=10),
#             robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=5, min_cluster_factor=0.1, skip_leaves=True, min_cluster_size=15),
#         ]
#
#         y_pred = None
#         best_score = -np.inf
#         for L in Ls:
#             print(".", end="", flush=True)
#             _y = L.fit_predict(X)
#             s1, s2 = treelhouette.treelhouette_score(L, skip_leaves=True)
#             s = s2  # s2 seems to work better
#             if best_score < -1 or best_score < s:
#                 best_score = s
#                 y_pred = _y
#
#         try:
#             res[K][f"Test_RobustSingleLinkage_Treelhouette"] = y_pred+1    # 0-based -> 1-based!!!
#         except Exception as e:
#             print("%s: %s" % (e.__class__.__name__, format(e)))
#
#     print(":<", end="", flush=True)
#     return res
