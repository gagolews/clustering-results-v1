"""
Copyright (C) 2026, Marek Gagolewski, https://www.gagolewski.com


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


# Two minimum spanning tree-based algorithms:
# 1. SequentialMST (SMST) by A. Layeb
#   Sequential MST Forest Clustering with Student-t Adaptive Stopping and Round-Robin Fair Growth, preprint, 2025
# 2. LDPMST — "Clustering with Local Density Peaks-Based Minimum Spanning Tree"
#   Cheng et al., IEEE Transactions on Knowledge and Data Engineering, 2021
#   DOI: 10.1109/TKDE.2019.2909055
# implemented by Abdesslem Layeb; see
# <https://github.com/Layebuniv/SequentialMSTclustering>.

import SequentialMSTclustering.smst.smst as smst
import SequentialMSTclustering.baselines.mst_baselines as bmst
import numpy as np


def do_benchmark_seqmst(X, Ks):
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    c = smst.SMST(assign_remaining=True)
    for K in Ks:
        method = "SeqMST"
        c.set_params(n_clusters=K)
        labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
        res[K][method] = labels_pred
        print(".", end="", flush=True)
    print("<", end="", flush=True)
    return res


def do_benchmark_ldpmst(X, Ks):
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        method = "LDPMST"
        c = bmst.LDPMST(n_clusters=K)
        labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
        res[K][method] = labels_pred
        print(".", end="", flush=True)
    print("<", end="", flush=True)
    return res


# does not allow n_clusters
# def do_benchmark_mstdc(X, Ks):
#     #max_K = max(max(Ks), 16) # just in case we'll need more in the future
#     #Ks = list(range(2, max_K+1))
#     res = dict()
#     for K in Ks: res[K] = dict()
#
#     print(" >:", end="", flush=True)
#     c = bmst.MSTDC()
#     for K in Ks:
#         method = "MSTDC"
#         c.set_params(n_clusters=K)
#         labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
#         res[K][method] = labels_pred
#         print(".", end="", flush=True)
#     print("<", end="", flush=True)
#     return res
