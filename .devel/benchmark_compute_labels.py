#!/usr/bin/env python3
#%%silent
#%%restart
#%%cd @


"""
Apply a registered (see below for details) clustering METHOD on
each benchmark dataset from the repository (see below) and
store the obtained partitions in the current working directory.

Copyright (C) 2020-2024, Marek Gagolewski, https://www.gagolewski.com

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


#import sys
import numpy as np
import pandas as pd
#import scipy.stats
import os.path
import glob
import re
import csv
import os
from natsort import natsorted
import sklearn.metrics
import time
from benchmark_load import *





# ``````````````````````````````````````````````````````````````````````````````
# `````` USER SETTINGS                                                   ```````
# ``````````````````````````````````````````````````````````````````````````````

# TODO: download the clustering benchmarks repository from
# https://github.com/gagolews/clustering_benchmarks_v1
benchmarks_path = "/home/gagolews/Projects/clustering-data-v1"


# TODO: select one or more processing methods  (must be a list)
preprocessors = ["original", "scale_standard", "scale_robust"][1:2]

# TODO: if your algorithm is too slow for processing of large datasets,
# well, set the following to True (will skip datasets with > 10000 rows)
small_only = True

# TODO: select one or more test batteries (must be a list)
batteries = ["wut", "graves", "other", "fcps", "sipu", "uci",
             "mnist", "h2mg", "g2mg"][:5]


# TODO: register new METHOD here, then select it
method = [
    "Genie",   # Genie - thresholds 0.1, 0.3, 0.5, 0.7, 1.0(=single linkage)
    "GIc",     # GIc - default parameters
    "Test_GIc", # GIc - many parameters (for testing)
    "Test_Genie_ForcedMerge", # Genie - experimental forced merge (for testing)
    "GenieApprox",
    "IcA",     # IcA (via GIc)
    "ITM",     # Andreas Mueller's Information Theoretic Clustering with MSTs
    "fastcluster_median",
    "fastcluster_centroid",
    "fastcluster_ward",
    "fastcluster_complete", # O(N^2) memory
    "fastcluster_average",  # O(N^2) memory
    "fastcluster_weighted", # O(N^2) memory
    "sklearn_kmeans",
    "sklearn_birch",
    "sklearn_gm",
    "sklearn_spectral",
    "fcps_nonproj",
][6]


# hdbscan.HDBSCAN -- doesn't allow for setting the desired number of clusters
#                 -- marks some points as noise in the output
# hdbscan.RobustSingleLinkage -- the same problem
# sklearn.cluster.OPTICS -- the same problem
# sklearn.cluster.AffinityPropagation -- no n_clusters
# sklearn.cluster.MeanShift -- no n_clusters
# sklearn.cluster.DBSCAN -- no n_clusters
#                        -- OPTICS and HDBSCAN should be better anyway



# TODO: register new do_benchmark() function here
if method == "Genie":
    import do_benchmark_genieclust
    do_benchmark = do_benchmark_genieclust.do_benchmark_genie
elif method == "GenieApprox":
    import do_benchmark_genieclust_test
    do_benchmark = do_benchmark_genieclust_test.do_benchmark_genieapprox
elif method == "Test_Genie_ForcedMerge":
    import do_benchmark_genieclust_test
    do_benchmark = do_benchmark_genieclust_test.do_benchmark_test_genie_forced_merge
elif method == "GIc":
    import do_benchmark_genieclust
    do_benchmark = do_benchmark_genieclust.do_benchmark_gic
elif method == "Test_GIc":
    import do_benchmark_genieclust_test
    do_benchmark = do_benchmark_genieclust_test.do_benchmark_test_gic
elif method == "IcA":
    import do_benchmark_genieclust
    do_benchmark = do_benchmark_genieclust.do_benchmark_ica
elif method == "ITM":
    import do_benchmark_itm
    do_benchmark = do_benchmark_itm.do_benchmark_itm
elif method == "sklearn_kmeans":
    import do_benchmark_sklearn
    do_benchmark = do_benchmark_sklearn.do_benchmark_kmeans
elif method == "sklearn_birch":
    import do_benchmark_sklearn
    do_benchmark = do_benchmark_sklearn.do_benchmark_birch
elif method == "sklearn_gm":
    import do_benchmark_sklearn
    do_benchmark = do_benchmark_sklearn.do_benchmark_gm
elif method == "sklearn_spectral":
    import do_benchmark_sklearn
    do_benchmark = do_benchmark_sklearn.do_benchmark_spectral
elif method == "fastcluster_average":
    import do_benchmark_fastcluster
    do_benchmark = do_benchmark_fastcluster.do_benchmark_average
elif method == "fastcluster_complete":
    import do_benchmark_fastcluster
    do_benchmark = do_benchmark_fastcluster.do_benchmark_complete
elif method == "fastcluster_weighted":
    import do_benchmark_fastcluster
    do_benchmark = do_benchmark_fastcluster.do_benchmark_weighted
elif method == "fastcluster_median":
    import do_benchmark_fastcluster
    do_benchmark = do_benchmark_fastcluster.do_benchmark_median
elif method == "fastcluster_ward":
    import do_benchmark_fastcluster
    do_benchmark = do_benchmark_fastcluster.do_benchmark_ward
elif method == "fastcluster_centroid":
    import do_benchmark_fastcluster
    do_benchmark = do_benchmark_fastcluster.do_benchmark_centroid
elif method == "fcps_nonproj":
    import do_benchmark_fcps
    do_benchmark = do_benchmark_fcps.do_benchmark_fcps_nonproj
else:
    raise Exception("unknown `method`")





"""
do_benchmark_METHOD(X, Ks) applies the clustering algorithm METHOD,
possibly with a few combinations of tunable parameters,
on the X dataset in order to determine the labels corresponding to
clusterings of different cardinalities.

It returns a Python dictionary res such that res[K]["METHOD_param1_param2"]
gives the label vector corresponding to a K-partition
for each K in Ks (optional other cardinalities can be considered as well).

Each label vector must be of length X.shape[0] (number of rows in X)
and must consist of integers from 1 to K (for a given K).
All the labels must be "saturated", i.e., occur at least once.

If a METHOD marks points as noise ones, these should not be included in the
label vectors; in other words, noise points should be added to some
clusters. In such a case, a special 1-partition (i.e., a label vector
corresponding to K=1) can be included that marks noise points as belonging
to cluster 0 and all the other ones as belonging to cluster 1.

If a METHOD has tunable parameters, they should be encoded
in a string of the form "METHOD_param1_..._paramM", with the underscore (_)
character acting as the parameter separator,
e.g., Complete_L1, Genie_G0.3_M7, Spectral_RBF_G0.5 etc.



These results will then generated by the benchmark() function
and saved as compressed CSV files
named ./PREPROCESS/METHOD/BATTERY/DATASET.resultK.gz, e.g.,
./original/Genie/sipu/aggregation.result7.gz for all the 7-partitions
obtained; the CSV file will have columns named
"METHOD_paramset1", "METHOD_paramset2" etc. corresponding to different
parameter combinations applied (each column gives a separate vector
of predicted labels).
"""




# ``````````````````````````````````````````````````````````````````````````````
# ````` BENCHMARK() PROCESSES A SINGLE DATASET                         `````````
# ``````````````````````````````````````````````````````````````````````````````


def benchmark(battery, dataset, benchmarks_path,
              method, do_benchmark,
              preprocess="original", small_only=False):
    """
    Processes a single benchmark dataset,
    calling do_benchmark(X, Ks).

    These results are saved as compressed CSV files
    named ./PREPROCESS/METHOD/BATTERY/DATASET.resultK.gz, where
    K is one of possibly many partition cardinalities generated.
    For instance, the path can be ./original/Genie/sipu/aggregation.result7.gz
    for all the 7-partitions obtained.

    The CSV file will have columns named "METHOD_paramset1", "METHOD_paramset2"
    etc. corresponding to different parameter combinations applied
    (each column gives a separate vector of predicted labels).



    Parameters
    ==========

    battery : str
        Name of the benchmark battery, e.g., 'sipu' or 'wut'.

    dataset : str
        Name of the dataset in the battery, e.g., 'spiral' or 'smile'.

    benchmarks_path : str
        Path to the local copy of the repository
        https://github.com/gagolews/clustering_benchmarks_v1

    method : str
        Name of the method family tested.

    do_benchmark : function
        A user-supplied function that takes two arguments X (a data matrix)
        and Ks (a list of partition cardinalities to generate)
        and returns a dictionary ret of dictionaries of integer (label) vectors,
        each of length X.shape[0], of the form ret[K]["method_params"]=labels.

    preprocess : one of "original", "scale_standard", "scale_robust"
        Each preprocessing method applies some basic transformations:
        it gets rid of columns of 0 variance,
        and adds a tiny bit of white noise.
        "scale_standard" is (x-mean(x))/sd(x, ddof=1);
        "scale_robust" is (x-median(x))/(1.4826*mad(x));
        for each column x in the dataset.
        "original" centres the points around the 0 vector and
        scales *all* columns proportionally (by the same factor)
        so that standard deviation of the whole dataset is equal to 1.

    small_only : bool, default False
        process datasets of up to 10000 elements only
    """
    input_fname_base = os.path.join(benchmarks_path, battery, dataset)

    np.random.seed(123)
    X = load_data(input_fname_base+".data.gz", preprocess)


    if small_only and X.shape[0] >= 10_000:
        return


    label_names = sorted([re.search(r"\.(labels[0-9]+)\.gz", name).group(1)
        for name in glob.glob(input_fname_base+".labels*.gz")])
    label_fnames = [input_fname_base+(".%s.gz" % name)
        for name in label_names]
    labels = [np.loadtxt(fname, dtype="int") for fname in label_fnames]

    # noise cluster == 0, don't count it.
    Ks = np.unique([len(np.bincount(l)[1:]) for l in labels])[::-1]
    # Ks is sorted decreasingly

    output_path = os.path.join(preprocess, method, battery)
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_fname_base = os.path.join(output_path, dataset)

    # get rid of K's that have already been computed
    which_K = np.array([
        os.path.exists(output_fname_base+(".result%d.gz"%K)) for K in Ks
    ])
    Ks = Ks[~which_K]

    print("## %-45s (n=%6d, Ks=%10r)" %
        ("%s/%s/%s/%s"%(preprocess, method, battery, dataset),
        X.shape[0], list(Ks)), end="", flush=True)

    if len(Ks) == 0:
        print(" (file already exists)", flush=True)
        return # nothing to do

    t0 = time.time()
    res = do_benchmark(X, Ks) # ---> call the user-supplied function <----------
    t1 = time.time()

    print(" (t=%.2f s)"%(t1-t0), flush=True)

    for K in res.keys():
        if len(res[K]) == 0:
            continue

        for m,l in res[K].items():
            assert len(l) == X.shape[0]
            if K > 0:
                assert min(l) == 1
                assert max(l) == K
                assert len(np.unique(l)) == K
            else:
                assert min(l) >= 0
                assert max(l) <= 1

        # this is a slow part, hold tight:
        output_fname = output_fname_base+(".result%d.gz"%K)
        res_df = pd.DataFrame.from_dict(res[K])
        res_df.to_csv(output_fname,
            quoting=csv.QUOTE_NONNUMERIC, index=False, compression="gzip")





# ``````````````````````````````````````````````````````````````````````````````
# ````````     MAIN: PROCESS ALL BENCHMARK DATASETS                    `````````
# ``````````````````````````````````````````````````````````````````````````````

if __name__ == "__main__":
    assert os.path.exists(benchmarks_path)
    assert type(preprocessors) is list
    assert type(batteries) is list
    assert type(method) is str
    assert do_benchmark # is defined

    # for every preprocessing scheme
    for preprocess in preprocessors:
        # for every battery of benchmark tests:
        for battery in batteries:
            fnames = glob.glob(os.path.join(benchmarks_path, battery, "*.data.gz"))
            datasets = natsorted([re.search(r"([^/]*)\.data\.gz", name)[1]
                                for name in fnames])

            # for every dataset in the benchmark battery:
            for dataset in datasets:
                try:
                    benchmark(battery, dataset, benchmarks_path,
                        method, do_benchmark, preprocess, small_only)
                except Exception as e:
                    print("%s: %s" % (e.__class__.__name__, format(e)))

    print("Done.")
