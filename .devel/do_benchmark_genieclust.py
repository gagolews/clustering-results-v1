"""
Copyright (C) 2020-2023, Marek Gagolewski, https://www.gagolewski.com


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



def do_benchmark_genie(X, Ks):
    max_K = max(Ks)
    max_K = max(max_K, 16) # just in case we'll need more in the future
    Ks = np.unique(np.array(list(range(2, max_K+1))+list(Ks)))
    res = dict()
    for K in Ks: res[K] = dict()

    genie = genieclust.Genie(
        postprocess="all"
    )

    print(" >:", end="", flush=True)
    for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
        method = "Genie_G%.1f"%g
        for K in Ks:
            genie.set_params(gini_threshold=g)
            genie.set_params(n_clusters=K)
            labels_pred = genie.fit_predict(X)+1 # 0-based -> 1-based!!!
            res[K][method] = labels_pred
        print(".", end="", flush=True)
    print(":<", end="", flush=True)
    return res



def do_benchmark_gic(X, Ks):
    max_K = max(Ks)
    #max_K = max(max_K, 16) # just in case we'll need more in the future
    #Ks = [0]+list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    # do not use compute_all_cuts! - see note on add_clusters in the manual
    gic = genieclust.GIc(
        compute_full_tree=False,
        compute_all_cuts=False,
        postprocess="all")

    print(" >:", end="", flush=True)
    for K in Ks:
        method = "GIc"
        gic.set_params(n_clusters=K)
        labels_pred = gic.fit_predict(X)+1 # 0-based -> 1-based!!!
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
        compute_full_tree=True,
        postprocess="all",
        compute_all_cuts=True,
        gini_thresholds=[] # this is IcA -- start from n singletons
    )

    print(" >:", end="", flush=True)
    method = "IcA"
    labels_pred_matrix = ica.fit_predict(X)+1 # 0-based -> 1-based!!!
    for K in Ks:
        res[K][method] = labels_pred_matrix[K]
    print(":<", end="", flush=True)
    return res
