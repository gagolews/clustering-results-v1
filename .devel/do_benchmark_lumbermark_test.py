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
import numpy as np
import sklearn.model_selection


def do_benchmark_test_lumbermark(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(    # TODO
        M=[1, 2, 4, 6, 8, 11, 16],
        min_cluster_factor=[0.05, 0.1, 0.15, 0.25, 0.33],
        mutreach_adj_type=["-c", "-d", "+d", "+c"][:1],
        #skip_leaves=[True],  #[True, False],  # False is worse
        # min_cluster_size=[10],  # not significant
    ))

    eps = 0.00000011920928955078125
    print(" >:", end="", flush=True)
    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)
            if param["mutreach_adj_type"] == "-d":
                mutreach_adj = -eps
            elif param["mutreach_adj_type"] == "+d":
                mutreach_adj = +eps
            elif param["mutreach_adj_type"] == "-c":
                mutreach_adj = -1-eps
            elif param["mutreach_adj_type"] == "+c":
                mutreach_adj = +1+eps
            else: stop("incorrect mutreach_adj")

            name = "f%g_M%d%s"%(param["min_cluster_factor"], param["M"], param["mutreach_adj_type"])
            try:
                y_pred = lumbermark.Lumbermark(
                    n_clusters=K,
                    postprocess="all",
                    M=param["M"],
                    min_cluster_factor=param["min_cluster_factor"],
                    quitefastmst_params=dict(mutreach_adj=mutreach_adj)
                ).fit_predict(X)    # TODO
                if max(y_pred) != K-1 and param["mutreach_adj_type"] == "-c":
                    y_pred = lumbermark.Lumbermark(
                        n_clusters=K,
                        postprocess="all",
                        min_cluster_size=5,
                        M=param["M"],
                        min_cluster_factor=param["min_cluster_factor"],
                        quitefastmst_params=dict(mutreach_adj=-eps)
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
