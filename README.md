# Benchmark Suite for Clustering Algorithms — Version 1 — Results

This repository features the outputs of various clustering algorithms
for the benchmark sets included in:

> M. Gagolewski and others (Eds.),
[Benchmark Suite for Clustering Algorithms – Version 1](https://github.com/gagolews/clustering_benchmarks_v1),
2020, doi:10.5281/zenodo.3815066

Refer to the corresponding
[README](https://github.com/gagolews/clustering_benchmarks_v1/blob/master/README.md)
file for more information on the methodology of supervised
evaluation of this class of unsupervised machine learning algorithms.

Currently, [genieclust](https://genieclust.gagolewski.com) (Genie)
outperforms (on average) all other algorithms.
You are free to use the results included herein when testing
your own clustering methods.
As a courtesy, please cite the benchmark battery and
some of the papers included in its
[Bibliography](https://github.com/gagolews/clustering_benchmarks_v1/blob/master/README.md#bibliography) section
as well as the papers introducing the algorithms you are comparing yourself to.




## Algorithms

The outputs of the following algorithms are included
(across a wide range of control parameters; note that we have only considered
the methods which allow for setting the precise number of generated clusters):

* [`genieclust`](https://genieclust.gagolewski.com)
    0.9.4 (Python; R version available too) — Genie, IcA, GIc,
    single linkage (Genie_1.0)

    * Marek Gagolewski. genieclust: Fast and robust hierarchical
    clustering. *SoftwareX*, 15:100722, 2021. doi:10.1016/j.softx.2021.100722.

    * M. Gagolewski, M. Bartoszuk, and A. Cena. Genie: A new, fast,
    and outlier-resistant hierarchical clustering algorithm.
    *Information Sciences*, 363:8–23, 2016. doi:10.1016/j.ins.2016.05.003.

    * A. Cena. *Adaptive hierarchical clustering algorithms based
    on data aggregation methods*, Ph.D. thesis, Systems Research Institute,
    Polish Academy of Sciences, 2018. In Polish.


* [`ITM`](https://github.com/amueller/information-theoretic-mst)
    git commit 178fd43 (Python)

    * A.C. Müller, S. Nowozin, and C.H. Lampert.
    *Information theoretic clustering using minimum spanning trees*.
    In *Proc. German Conference on Pattern Recognition*. 2012.
    URL: https://github.com/amueller/information-theoretic-mst.


* [`sklearn`](https://scikit-learn.org/stable/modules/clustering.html)
    0.23.1 (Python) — k-means, spectral, Gaussian mixtures, Birch

    * F. Pedregosa and others. Scikit-learn: Machine learning in Python.
    *Journal of Machine Learning Research*, 12(85):2825–2830, 2011.
    URL: http://jmlr.org/papers/v12/pedregosa11a.html.

    * L. Buitinck and others. *API design for machine learning software:
    Experiences from the scikit-learn project*. In *ECML PKDD Workshop:
    Languages for Data Mining and Machine Learning*, 108–122. 2013.


* [`fastcluster`](http://www.danifold.net/fastcluster.html) 1.1.26
    (Python; R version available too) — average, centroid, complete,
    median, Ward, weighted/McQuitty linkage

    * D. Müllner. fastcluster: Fast hierarchical, agglomerative clustering
    routines for R and Python. *Journal of Statistical Software*,
    53(9):1–18, 2013. doi:10.18637/jss.v053.i09.


* [`optim_cvi`](https://github.com/gagolews/optim_cvi) — argmaxes of
    many internal cluster validity measures,
    including the Caliński-Harabasz, Dunn, or silhouette index

    * M. Gagolewski, M. Bartoszuk, A. Cena,
    Are cluster validity measures (in)valid?,
    2021, *under review*.

If you wish other results be included in this repository,
do not hesitate to contact the [maintainer](https://www.gagolewski.com)
(Marek Gagolewski).



## *Original* Data Spaces

The subdirectory named `results_original` includes the clusterings
of the *original* data spaces, i.e., with only some minor preprocessing
in place:

* columns of zero variance have been removed;
* tiny amount of white noise has been added to each datum to make sure the
    distance matrices have all unique elements (this guarantees the
    results of hierarchical clustering algorithms are unambiguous);
* all data were translated and scaled proportionally
    to assure that each column is of mean 0 and that the total (not: per column,
    hence this is not the same as standardisation) variance is 1.

```python
def load_data(fname, preprocess):
    """
    Loads the data matrix and preprocesses it.
    """
    X = np.loadtxt(fname, ndmin=2)

    X = X[:, X.var(axis=0) > 0] # remove all columns of 0 variance
    # add a tiny bit of white noise:
    X += np.random.normal(0.0, X.std(ddof=1)*1e-6, size=X.shape)

    if preprocess == "original":
        s = X.std(axis=None, ddof=1) # scale all columns proportionally
        X = (X-X.mean(axis=0))/s
    else:
        raise Exception("unknown `preprocess`")

    X = X.astype(np.float32, order="C", copy=False) # work with float32

    return X
```

Note, however, that spectral clustering (results included herein)
can be considered as one that modifies the input data space.



## File Format

Each file is named like `results_original/method/battery/datasetK.gz`,
where K is the number of identified clusters, e.g.,
`results_original/Genie/wut/labirynth4.gz`.

It is a gzipped-CSV file where columns are label vectors with elements
in 1..K. Each column represents the output of an algorithm
with a different parameter setting (e.g., `Genie_0.1`, `Genie_0.3`, etc. –
first row gives the method name).


For example:

```
"Genie_G0.1","Genie_G0.3","Genie_G0.5","Genie_G0.7","Genie_G1.0"  <--- names
1,1,1,1,1
2,2,2,2,2
3,3,3,3,3
4,1,1,1,1
2,2,2,2,2
3,3,3,3,3
4,1,1,1,1  <--- Genie_G0.1 claims the 7th data point belongs to the 4th cluster
2,2,2,2,2
3,3,3,3,3
...        <--- As many rows as data points in total (plus names in the 1st row)
```


For some (slower, memory consuming) methods we give the results only for
the smaller datasets together with the cardinalities corresponding to the
true (reference) label vectors from the
[benchmark repository](https://github.com/gagolews/clustering_benchmarks_v1).



Subdirectory `catalogue_original` contains the graphical representations
of the identified clusters for quite a few 2- and 3-dimensional data sets
and methods.
