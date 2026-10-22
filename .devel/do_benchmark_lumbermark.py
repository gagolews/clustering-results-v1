"""
Copyright (C) 2020-2026, Marek Gagolewski, https://www.gagolewski.com


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

import lumbermark
import numpy as np
import sklearn.model_selection
import numpy as np
import quitefastmst
import scipy.spatial.distance


def do_benchmark_lumbermark(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(
        M=[0, 1, 3, 5, 7, 10, 15, 25][::-1],
        min_cluster_factor=[0.05, 0.1, 0.15, 0.2, 0.25, 0.33, 0.5],
    ))
    print(" >:", end="", flush=True)

    l = lumbermark.Lumbermark(
        quitefastmst_params=dict(algorithm="brute") if X.shape[0] <= 10_000 else dict()
    )

    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)

            name = "f%g_M%d"%(
                param["min_cluster_factor"],
                param["M"],
            )

            l.set_params(n_clusters=K)
            l.set_params(M=param["M"])
            l.set_params(min_cluster_factor=param["min_cluster_factor"])

            try:
                for min_cluster_size in [10, 5]:
                    l.set_params(min_cluster_size=min_cluster_size)
                    y_pred = l.fit_predict(X)

                    if max(y_pred) == K-1: break

                if max(y_pred) != K-1: stop()

                res[K][f"Lumbermark_{name}"] = y_pred+1    # 0-based -> 1-based!!!
            except Exception as e:
                print("%s: %s (%r)" % (e.__class__.__name__, format(e), repr(param)))


    print(":<", end="", flush=True)
    return res


def do_benchmark_test_lumbermark(X, Ks):
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(
        mutreach_ties=["dcore_min0", "dist_max0", "dist_min0", "dcore_max0",
                       "dcore_min+", "dist_max+", "dist_min+", "dcore_max+"],
        M=[0, 3, 5, 7, 10, 15, 25][::-1],
        min_cluster_factor=[0.15, 0.2, 0.25, 0.33],
        skip_leaves=[True, False],
        nested=[False, True],
        # min_cluster_size=[10],  # not significant
    ))
    print(" >:", end="", flush=True)

    l = lumbermark.Lumbermark(
        quitefastmst_params=dict(algorithm="brute")
    )

    for K in Ks:
        print(" ", end="", flush=True)
        for param in param_grid:
            print(".", end="", flush=True)

            name = "f%g_M%d_n%d_sl%d_%s"%(
                param["min_cluster_factor"],
                param["M"],
                int(param["nested"]),
                int(param["skip_leaves"]),
                param["mutreach_ties"],
            )

            l.set_params(M=param["M"])
            l.set_params(n_clusters=K)
            l.set_params(min_cluster_factor=param["min_cluster_factor"])
            l.set_params(nested=param["nested"])
            l.set_params(skip_leaves=param["skip_leaves"])
            l.set_params(quitefastmst_params=dict(
                algorithm="brute",
                mutreach_ties=param["mutreach_ties"][:-1],
                mutreach_leaves="keep" if param["mutreach_ties"][-1] == "0" else "reconnect_dcore_min"
            ))

            try:
                for min_cluster_size in [10, 5, 2]:
                    l.set_params(min_cluster_size=min_cluster_size)
                    y_pred = l.fit_predict(X)

                    if max(y_pred) == K-1: break

                if max(y_pred) != K-1: stop()

                res[K][f"TestLumbermark_{name}"] = y_pred+1    # 0-based -> 1-based!!!
            except Exception as e:
                print("%s: %s (%r)" % (e.__class__.__name__, format(e), repr(param)))


    print(":<", end="", flush=True)
    return res
