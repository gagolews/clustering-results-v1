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



import fastcluster
import numpy as np
import warnings
import scipy.cluster.hierarchy



def __do_benchmark_fastcluster(X, Ks, linkage):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()
    method = "fastcluster_%s"%linkage

    print(" >:", end="", flush=True)

    if linkage in ["median", "ward", "centroid"]:
        linkage_matrix = fastcluster.linkage_vector(X, method=linkage)
    else: # these compute the whole distance matrix
        linkage_matrix = fastcluster.linkage(X, method=linkage)

    print(".", end="", flush=True)

    # correction for the departures from ultrametricity -- cut_tree needs this.
    linkage_matrix[:,2] = np.maximum.accumulate(linkage_matrix[:,2])
    labels_pred_matrix = scipy.cluster.hierarchy.\
        cut_tree(linkage_matrix, n_clusters=Ks)+1 # 0-based -> 1-based!!!

    for k in range(len(Ks)):
        res[Ks[k]][method] = labels_pred_matrix[:,k]

    print(":<", end="", flush=True)
    return res


def do_benchmark_complete(X, Ks):
    return __do_benchmark_fastcluster(X, Ks, "complete")

def do_benchmark_average(X, Ks):
    return __do_benchmark_fastcluster(X, Ks, "average")

def do_benchmark_weighted(X, Ks):
    return __do_benchmark_fastcluster(X, Ks, "weighted")

def do_benchmark_median(X, Ks):
    return __do_benchmark_fastcluster(X, Ks, "median")

def do_benchmark_ward(X, Ks):
    return __do_benchmark_fastcluster(X, Ks, "ward")

def do_benchmark_centroid(X, Ks):
    return __do_benchmark_fastcluster(X, Ks, "centroid")
