"""
Copyright (C) 2020, Marek Gagolewski, https://www.gagolewski.com


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


# pip3 install fast-ldp-mst-clustering
# https://pypi.org/project/fast-ldp-mst-clustering/
# https://github.com/Teng-Qiu-Clustering/Fast-LDP-MST-Clustering-IEEE-TKDE-2022
# Teng Qiu, Yongjie Li, IEEE Transactions on Knowledge and Data Engineering, 2022, DOI: 10.1109/TKDE.2022.3150403

# On some datasets, the algorithm fails to converge;
# we try to fix this by increasing the number of NNs, but there is no guarantee

import fast_ldp_mst_clustering.fast_ldp_mst_clustering as clmod
import numpy as np


def do_benchmark_fastldpmst(X, Ks):
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        method = "FastLDPMST"
        eta = max(1, int(0.01*X.shape[0])) # A threshold for the cluster size (setting from the paper)
        nns = max(1, int(np.ceil(np.log2(X.shape[0])))) # Number of NNs (setting from the paper)
        nns_max = nns*4
        while nns <= nns_max:
            try:
                c, f, TotalTime = clmod.FastLDPMST(X, K, eta, nns, "KD-tree")
                assert np.min(c) == 0
                assert np.max(c) == K-1
                assert np.all(np.bincount(c) > 0)
                labels_pred = c+1 # 0-based -> 1-based
                break
            except:
                print("X", end="", flush=True)
                nns += 1
                continue
        else:
            raise Exception("fail")

        res[K][method] = labels_pred
        print(".", end="", flush=True)
    print("<", end="", flush=True)
    return res
