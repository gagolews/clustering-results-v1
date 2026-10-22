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


# SNN-DPC
# <https://github.com/liurui39660/SnnDpc> commit 2e75cd3 Sep 15, 2020
# Rui Liu, Hong Wang, Xiaomei Yu, Shared-nearest-neighbor-based clustering by fast search and find of density peaks, Information Sciences 450, 2018, 200-226, DOI:10.1016/j.ins.2018.03.031

from SNNDPC.SNNDPC import SNNDPC
import numpy as np


"for the SNN-DPC and FKNN-DPC algorithms, since they have only one integer argument k, we select the argument continuously from 4 to 50. The lower bound is 4 because, for some datasets, a small k may lead the algorithm to become endless and cause an error. For the upper bound, a large k fails to significantly affect the results of the algorithms, making it less meaningful to be further tested"

def do_benchmark_snndpc(X, Ks):
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        for nns in [3, 5, 7, 10, 15, 25, 50]:
            method = "SNNDPC_%d" % nns
            try:
                indexCentroid, c = SNNDPC(nns, K, X)
                assert np.min(c) == 0
                assert np.max(c) == K-1
                assert np.all(np.bincount(c) > 0)
                labels_pred = c+1 # 0-based -> 1-based
            except:
                print("X", end="", flush=True)

            res[K][method] = labels_pred
            print(".", end="", flush=True)
        print(":", end="", flush=True)
    print("<", end="", flush=True)
    return res
