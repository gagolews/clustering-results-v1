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



import genieclust
import numpy as np


def do_benchmark_test_geniem(X, Ks):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = [0]+list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    genie = genieclust.Genie(
        n_clusters=max_K,
        #compute_full_tree=True,
        postprocess="all",
        compute_all_cuts=True
    )

    print(" >:", end="", flush=True)
    eps = 0.00000011920928955078125
    for mutreach_adj_type in ["-c", "-d", "+d", "+c"][:1]:
        for M in sorted([1, 2, 4, 6, 8, 11, 16])[::-1]:  # decreasing M => NNs are reused
            for g in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
                method = "GenieM_G%g_M%d%s"%(g, M, mutreach_adj_type)
                if mutreach_adj_type == "-d":
                    mutreach_adj = -eps
                elif mutreach_adj_type == "+d":
                    mutreach_adj = +eps
                elif mutreach_adj_type == "-c":
                    mutreach_adj = -1-eps
                elif mutreach_adj_type == "+c":
                    mutreach_adj = +1+eps
                else: stop("incorrect mutreach_adj")

                genie.set_params(gini_threshold=g, M=M, quitefastmst_params=dict(mutreach_adj=mutreach_adj))
                labels_pred_matrix = genie.fit_predict(X)+1  # 0-based -> 1-based!!!
                # note some K-partitions might be unavailable (too many noise points):
                for K in range(labels_pred_matrix.shape[0]):
                    if K == 1: continue # ignore
                    res[K][method] = labels_pred_matrix[K]
            print(".", end="", flush=True)
        print(":", end="", flush=True)
    print("<", end="", flush=True)
    return res
