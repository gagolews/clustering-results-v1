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




import sklearn.cluster
import sklearn.mixture
import numpy as np
import warnings

def do_benchmark_birch(X, Ks):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for branching_factor in [10, 50, 100]:
        for threshold in [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]:
            for K in Ks:
                method = "sklearn_birch_T%g_BF%d"%(threshold, branching_factor)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    # If threshold is too large, the number of subclusters
                    # found might be less than the requested one.
                    c = sklearn.cluster.Birch(n_clusters=K,
                        threshold=threshold,
                        branching_factor=branching_factor
                    )
                    labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
                    #print(np.bincount(labels_pred))
                    #print(len(labels_pred))
                    if labels_pred.max() == K:
                        res[K][method] = labels_pred
            print(".", end="", flush=True)
        print(":", end="", flush=True)
    print("<", end="", flush=True)
    return res


def do_benchmark_kmeans(X, Ks):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        method = "sklearn_kmeans"
        c = sklearn.cluster.KMeans(n_clusters=K,
             # defaults: n_init=10, max_iter=300, tol=1e-4, init="k-means++"
            random_state=123
        )
        labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
        res[K][method] = labels_pred
        print(".", end="", flush=True)
    print("<", end="", flush=True)
    return res


def do_benchmark_spectral(X, Ks):
    # this is slow -- use only Ks provided
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1))

    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        for affinity in ["rbf", "laplacian", "poly", "sigmoid"]:
            for gamma in [0.25, 0.5, 1.0, 2.5, 5.0]:
                method = "sklearn_spectral_A%s_G%g"%(affinity, gamma)
                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        c = sklearn.cluster.SpectralClustering(n_clusters=K,
                            affinity=affinity, gamma=gamma,
                            random_state=123
                        )
                        labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
                        #print(np.bincount(labels_pred))
                        #print(len(labels_pred))
                        assert min(labels_pred) == 1
                        assert max(labels_pred) == K
                        assert labels_pred.shape[0] == X.shape[0]
                        assert len(np.unique(labels_pred)) == K
                        res[K][method] = labels_pred
                        print(".", end="", flush=True)
                except:
                    print("x", end="", flush=True)
        print(":", end="", flush=True)
    print("<", end="", flush=True)
    return res


def do_benchmark_gm(X, Ks):
    max_K = max(max(Ks), 16) # just in case we'll need more in the future
    Ks = list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()

    print(" >:", end="", flush=True)
    for K in Ks:
        method = "sklearn_gm"
        c = sklearn.mixture.GaussianMixture(n_components=K,
            n_init=100,
            # defaults: tol=1e-3, covariance_type="full", max_iter=100, reg_covar=1e-6
            random_state=123
        )
        labels_pred = c.fit_predict(X)+1 # 0-based -> 1-based
        if len(np.unique(labels_pred)) != K: # some clusters might be empty
            continue # skip
        res[K][method] = labels_pred
        print(".", end="", flush=True)
    print("<", end="", flush=True)
    return res


