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
    max_K = max(max_K, 16)  # just in case we'll need more in the future
    Ks = np.unique(np.array(list(range(2, max_K+1))+list(Ks)))
    res = dict()
    for K in Ks: res[K] = dict()

    genie = genieclust.Genie(
        postprocess="all"
    )

    print(" >:", end="", flush=True)
    for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
        method = "Genie_G%.1f" % g
        for K in Ks:
            genie.set_params(gini_threshold=g)
            genie.set_params(n_clusters=K)
            labels_pred = genie.fit_predict(X) + 1 # 0-based -> 1-based!!!
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





from estimate_dimension import *

def do_benchmark_test_gic(X, Ks):
    max_K = max(Ks)
    #max_K = max(max_K, 16) # just in case we'll need more in the future
    #Ks = [0]+list(range(2, max_K+1))
    res = dict()
    for K in Ks: res[K] = dict()


    # do not use compute_all_cuts! - see note on add_clusters in the manual
    gic = genieclust.GIc(postprocess="all")

    print(" >:", end="", flush=True)
    #di = estimate_dimension(X)
    print(":", end="", flush=True)

    # NOTE: n_features = None turns out to be slightly better than "i" and "r"
    #for d in ["d"]:  # ["d", "i", "r"]:
        #if   d == "d": n_features = None
        #elif d == "i": n_features = di
        #else:          n_features = np.round(di)

    n_features = None

    for add in [10, 5, 1, 0]:
        for g in [np.r_[0.1, 0.3, 0.5, 0.7], np.linspace(0.0, 1.0, 11)]:
            for K in Ks:
                #method = "Test_GIc_A%d_T%d_D%s"%(add, len(g), d)
                method = "Test_GIc_Addcl%d_Thresnum%d"%(add, len(g))
                gic.set_params(n_clusters=K,
                        compute_full_tree=False,
                        compute_all_cuts=False,
                        n_features=n_features,
                        gini_thresholds=g,
                        add_clusters=add)
                labels_pred = gic.fit_predict(X)+1 # 0-based -> 1-based!!!
                res[K][method] = labels_pred
        print(".", end="", flush=True)
    print(":", end="", flush=True)

    # gic.set_params(
    #     n_clusters=max_K,
    #     compute_full_tree=True,
    #     compute_all_cuts=True,
    #     gini_thresholds=[]  # this is IcA -- start from n singletons
    # )
    # method = "Test_IcA_D%s"%d
    # labels_pred_matrix = gic.fit_predict(X)+1 # 0-based -> 1-based!!!
    # for K in Ks:
    #     res[K][method] = labels_pred_matrix[K]
    # print(":", end="", flush=True)

    print("<", end="", flush=True)
    return res



def do_benchmark_test_genie_forced_merge(X, Ks):
    max_K = max(Ks)
    max_K = max(max_K, 16)  # just in case we'll need more in the future
    Ks = np.unique(np.array(list(range(2, max_K+1))+list(Ks)))
    res = dict()
    for K in Ks: res[K] = dict()

    genie = genieclust.Genie(
        postprocess="all"
    )

    genie._experimental_forced_merge = True

    print(" >:", end="", flush=True)
    for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
        method = "Test_Genie_ForcedMerge_G%.1f"%g
        for K in Ks:
            genie.set_params(gini_threshold=g)
            genie.set_params(n_clusters=K)
            labels_pred = genie.fit_predict(X)+1 # 0-based -> 1-based!!!
            res[K][method] = labels_pred
        print(".", end="", flush=True)
    print(":<", end="", flush=True)
    return res




def do_benchmark_genieapprox(X, Ks):
    max_K = max(Ks)
    max_K = max(max_K, 16) # just in case we'll need more in the future
    Ks = np.unique(np.array(list(range(2, max_K+1))+list(Ks)))
    res = dict()
    for K in Ks: res[K] = dict()


    print(" >:", end="", flush=True)
    for s in range(10):
        np.random.seed(s+1)
        genie = genieclust.Genie(
            postprocess="all",
            exact=False
        )
        for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
            method = "GenieApprox_G%.1f_s%d"%(g,s)
            for K in Ks:
                genie.set_params(gini_threshold=g)
                genie.set_params(n_clusters=K)
                labels_pred = genie.fit_predict(X)+1 # 0-based -> 1-based!!!
                res[K][method] = labels_pred
        print(".", end="", flush=True)
    print(":<", end="", flush=True)
    return res


#def do_benchmark_gicm(X, Ks):
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1)) # the 0-clustering won't be needed
    #res = dict()
    #for K in Ks: res[K] = dict()

    ## do not use compute_all_cuts! - see note on add_clusters in the manual
    #gic = genieclust.GIc(compute_full_tree=False, postprocess="all")

    #print(" >:", end="", flush=True)
    #for M in sorted([1, 3, 5, 9, 15, 25])[::-1]: # decreasing M => NNs are reused
        #for add in [5, 1, 0]:
            #for g in [np.r_[0.1, 0.3, 0.5, 0.7], np.linspace(0.0, 1.0, 11), []]:
                #if len(g) == 0 and add > 0: continue
                #for K in Ks:
                    #method = "GIc_A%d_T%d_M%d"%(add,len(g),M)
                    #gic.set_params(n_clusters=K,
                        #gini_thresholds=g, add_clusters=add, M=M)
                    #labels_pred = gic.fit_predict(X)+1 # 0-based -> 1-based!!!
                    #if gic.n_clusters_ == K:
                        ## due to noise points, some K-partitions might be unavailable
                        #res[K][method] = labels_pred
                #print(".", end="", flush=True)
        #print(":", end="", flush=True)
    #print("<", end="", flush=True)
    #return res



#def do_benchmark_geniem(X, Ks):
    #max_K = max(max(Ks), 16) # just in case we'll need more in the future
    #Ks = [0]+list(range(2, max_K+1))
    #res = dict()
    #for K in Ks: res[K] = dict()

    #genie = genieclust.Genie(
        #n_clusters=max_K,
        #compute_full_tree=True,
        #postprocess="all",
        #compute_all_cuts=True
    #)


    #print(" >:", end="", flush=True)
    #for M in sorted([1, 3, 5, 9, 15, 25])[::-1]: # decreasing M => NNs are reused
        #for g in [0.1, 0.3, 0.5, 0.7, 1.0]:
            #method = "Genie_G%.1f_M%d"%(g,M)
            #genie.set_params(gini_threshold=g, M=M)
            #labels_pred_matrix = genie.fit_predict(X)+1 # 0-based -> 1-based!!!
            ## note some K-partitions might be unavailable (too many noise points):
            #for K in range(labels_pred_matrix.shape[0]):
                #if K == 1: continue # ignore
                #res[K][method] = labels_pred_matrix[K]
            #print(".", end="", flush=True)
        #print(":", end="", flush=True)
    #print("<", end="", flush=True)
    #return res
