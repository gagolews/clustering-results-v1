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


import genieclust
import numpy as np
import sklearn


def do_benchmark_genie(X, Ks):
    max_K = max(Ks)
    max_K = max(max_K, 16) # just in case we'll need more in the future
    Ks = np.unique(np.array(list(range(2, max_K+1))+list(Ks)))
    res = dict()
    for K in Ks: res[K] = dict()

    genie = genieclust.Genie()

    print(" >:", end="", flush=True)
    for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
        method = "Genie_G%.1f"%g
        for K in Ks:
            genie.set_params(gini_threshold=g)
            genie.set_params(n_clusters=K)
            labels_pred = genie.fit_predict(X)+1  # 0-based -> 1-based!!!
            res[K][method] = labels_pred
        print(".", end="", flush=True)
    print(":<", end="", flush=True)
    return res


def do_benchmark_geniem(X, Ks):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    param_grid = sklearn.model_selection.ParameterGrid(dict(
        M=[1, 3, 5, 7, 10, 15, 25][::-1],
        gini_threshold=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
    ))

    genie = genieclust.Genie(
        n_clusters=max_K,
        coarser=True,
        quitefastmst_params=dict(algorithm="brute"),
    )

    print(" >:", end="", flush=True)
    for param in param_grid:
        print(".", end="", flush=True)
        name = "Genie_G%g_M%d"%(
            param["gini_threshold"], param["M"]
        )

        genie.set_params(
            gini_threshold=param["gini_threshold"],
            M=param["M"]
        )

        genie.fit(X)
        labels_pred_matrix = genie.labels_matrix_ + 1  # 0-based -> 1-based!!!
        # note that some K-partitions might be unavailable (too many noise points):
        for K in range(1, labels_pred_matrix.shape[0]):
            res[K+1][name] = labels_pred_matrix[K]

        print(":", end="", flush=True)
    print("<", end="", flush=True)
    return res


def do_benchmark_gic(X, Ks):
    max_K = max(Ks)
    #max_K = max(max_K, 16) # just in case we'll need more in the future
    #Ks = [0]+list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    # do not use compute_all_cuts! - see note on add_clusters in the manual
    gic = genieclust.GIc(
        compute_full_tree=False
    )

    print(" >:", end="", flush=True)
    for K in Ks:
        method = "GIc"
        gic.set_params(n_clusters=K)
        labels_pred = gic.fit_predict(X)+1  # 0-based -> 1-based!!!
        if gic.n_clusters_ == K:
            # due to noise points, some K-partitions might be unavailable
            res[K][method] = labels_pred
    print(":<", end="", flush=True)
    return res




def do_benchmark_ica(X, Ks):
    max_K = max(Ks)
    #max_K = max(max_K, 16) # just in case we'll need more in the future
    #Ks = [0]+list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    ica = genieclust.GIc(
        n_clusters=max_K,
        gini_thresholds=[] # this is IcA -- start from n singletons
    )

    print(" >:", end="", flush=True)
    method = "IcA"
    labels_pred_matrix = ica.fit_predict(X)+1  # 0-based -> 1-based!!!
    for K in Ks:
        res[K][method] = labels_pred_matrix[K]
    print(":<", end="", flush=True)
    return res
