# [A Framework for Benchmarking Clustering Algorithms](https://clustering-benchmarks.gagolewski.com)
## Results for Benchmark Suite Version 1

This repository is part of the
[**Framework for Benchmarking Clustering Algorithms**](https://clustering-benchmarks.gagolewski.com).

This directory hosts the outputs of various clustering algorithms
for the datasets included in the *Benchmark Suite for Clustering Algorithms:
Version 1.1.0*, 2022, <https://github.com/gagolews/clustering-data-v1/>.

The algorithms operated on the *original* data spaces,
i.e., where only some minor preprocessing was applied:

* columns of zero variance have been removed;
* tiny amount of white noise has been added to each datum to make sure the
    distance matrices consist of unique elements (this guarantees that the
    results of hierarchical clustering algorithms are unambiguous);
* all data were translated and scaled proportionally
    to assure that each column is of mean 0 and that the total variance
    of *all* entries is 1 (this is not standardisation).


More precisely:

```python
def load_data(fname, preprocess):
    """
    Loads the data matrix and pre-processes it.
    """
    X = np.loadtxt(fname, ndmin=2)

    X = X[:, X.var(axis=0) > 0]  # remove all columns of 0 variance
    # add a tiny bit of white noise:
    X += np.random.normal(0.0, X.std(ddof=1)*1e-6, size=X.shape)

    if preprocess == "original":
        s = X.std(axis=None, ddof=1)  # scale all columns proportionally
        X = (X-X.mean(axis=0))/s
    else:
        raise Exception("unknown `preprocess`")

    X = X.astype(np.float32, order="C", copy=False)  # work with float32

    return X
```
