# README

Results for benchmark sets included in:

> M. Gagolewski and others (Eds.),
[Benchmark Suite for Clustering Algorithms – Version 1](https://github.com/gagolews/clustering_benchmarks_v1),
2020, doi:10.5281/zenodo.3815066

There are the *original* data spaces, i.e., only some minor preprocessing
was done:

* columns of zero variance have been removed;
* tiny amount of white noise has been added to each datum to make sure the
    distance matrices have all unique elements (this guarantees the
    results of hierarchical clustering algorithms are unambiguous);
* all data were translated and scaled proportionally
    to assure that each column is of mean 0 and that the total (not: per column,
    hence this is not standardisation) variance is 1.


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
