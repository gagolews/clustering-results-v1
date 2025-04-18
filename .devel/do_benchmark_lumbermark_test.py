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
sys.path.append("/home/gagolews/Python/genieclust/.devel")
sys.setrecursionlimit(100000)


import genieclust
import lumbermark
import treelhouette
import robust_single_linkage
import numpy as np
import sklearn.model_selection


def do_benchmark_test_lumbermark(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(
        min_cluster_size=[1, 5, 10, 15],
        min_cluster_factor=[0, 0.05, 0.1, 0.15, 0.2, 0.25],
        skip_leaves=[True, False],
        n_neighbors=[3, 5, 7, 10, 15, None],
        noise_threshold=["half", "uhalf", "-1", "0", "1", "2"],
        noise_postprocess=["tree", "closest"],
    ))

    print(" >:", end="", flush=True)
    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)
            name = ",".join(["%r" % v for v in param.values()])
            try:
                res[K][f"Test_Lumbermark_{name}"] = lumbermark.Lumbermark(n_clusters=K, **param).fit_predict(X)  # TODO: 1->0 based
            except Exception as e:
                    print("%s: %s" % (e.__class__.__name__, format(e)))

    print(":<", end="", flush=True)
    return res



def do_benchmark_test_robustsl(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(
        min_cluster_size=[1, 5, 10, 15],
        min_cluster_factor=[0, 0.05, 0.1, 0.15, 0.2, 0.25],
        skip_leaves=[True, False],
        M=[1, 4, 6, 8, 11, 16, None]
    ))

    print(" >:", end="", flush=True)
    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)
            name = ",".join(["%r" % v for v in param.values()])
            try:
                res[K][f"Test_RobustSingleLinkage_{name}"] = robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, **param).fit_predict(X)  # TODO: 1->0 based
            except Exception as e:
                    print("%s: %s" % (e.__class__.__name__, format(e)))

    print(":<", end="", flush=True)
    return res


def do_benchmark_test_robustsl_treelhouette(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        print(" ", end="", flush=True)
        Ls = [
            #robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=1, min_cluster_factor=0.25, skip_leaves=False, min_cluster_size=10),
            #robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=1, min_cluster_factor=0.1, skip_leaves=False, min_cluster_size=15),
            robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=5, min_cluster_factor=0.25, skip_leaves=True, min_cluster_size=10),
            robust_single_linkage.RobustSingleLinkageClustering(n_clusters=K, M=5, min_cluster_factor=0.1, skip_leaves=True, min_cluster_size=15),
        ]

        y_pred = None
        best_score = -np.inf
        for L in Ls:
            print(".", end="", flush=True)
            _y = L.fit_predict(X)
            s1, s2 = treelhouette.treelhouette_score(L, skip_leaves=True)
            s = s2  # s2 seems to work better
            if best_score < -1 or best_score < s:
                best_score = s
                y_pred = _y

        try:
            res[K][f"Test_RobustSingleLinkage_Treelhouette"] = y_pred
        except Exception as e:
            print("%s: %s" % (e.__class__.__name__, format(e)))

    print(":<", end="", flush=True)
    return res
