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



# linkage_matrix computations are based on the code
# by Mathew Kallada, Andreas Mueller (License: BSD 3 clause)
# https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html


import sklearn.cluster
import numpy as np
import warnings
import scipy.cluster.hierarchy


def __do_benchmark_agglomerative(X, Ks, linkage):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()
    method = "agglomerative_%s"%linkage

    print(" >:", end="", flush=True)

    c = sklearn.cluster.AgglomerativeClustering(
        distance_threshold=0,
        n_clusters=None,
        compute_full_tree=True,
        linkage=linkage
    )
    c.fit(X)
    print(":", end="", flush=True)

    #```````````````````````````````````````````````````````````````````````````
    # See https://scikit-learn.org/stable/_downloads/6c3126e55d97d68efdd8da229311ac00/plot_agglomerative_dendrogram.py
    # create the counts of samples under each node::
    counts = np.zeros(c.children_.shape[0])
    n_samples = len(c.labels_)
    for i, merge in enumerate(c.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count
    #```````````````````````````````````````````````````````````````````````````


    linkage_matrix = np.column_stack([c.children_, c.distances_,
                                      counts]).astype(float)

    labels_pred_matrix = scipy.cluster.hierarchy.\
        cut_tree(linkage_matrix, n_clusters=Ks)+1 # 0-based -> 1-based!!!
    for k in range(len(Ks)):
        res[Ks[k]][method] = labels_pred_matrix[:,k]

    print("<", end="", flush=True)
    return res



def do_benchmark_average(X, Ks):
    return __do_benchmark_agglomerative(X, Ks, "average")


def do_benchmark_complete(X, Ks):
    return __do_benchmark_agglomerative(X, Ks, "complete")


def do_benchmark_ward(X, Ks):
    return __do_benchmark_agglomerative(X, Ks, "ward")
