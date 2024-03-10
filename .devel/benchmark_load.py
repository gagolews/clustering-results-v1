"""
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



import numpy as np
import scipy.stats


def load_data(fname, preprocess):
    """
    Loads the data matrix and preprocesses it, see benchmark() for more details.
    """
    X = np.loadtxt(fname, ndmin=2)

    X = X[:, X.var(axis=0) > 0] # remove all columns of 0 variance
    # add a tiny bit of white noise:
    X += np.random.normal(0.0, X.std(ddof=1)*1e-6, size=X.shape)

    if preprocess == "scale_standard": # mean/sd
        s = X.std(axis=0, ddof=1)
        X = (X-X.mean(axis=0))/s
    elif preprocess == "scale_robust": # median/(1.4826*MAD)
        s = np.median(np.abs(X-np.median(X, axis=0)), axis=0)
        s = s/scipy.stats.norm().ppf(0.75) # i.e., s*1.4826
        s[s<1e-12] = 1.0 # don't scale columns of zero MAD
        X = (X-np.median(X, axis=0))/s
    elif preprocess == "original":
        s = X.std(axis=None, ddof=1) # scale all columns proportionally
        X = (X-X.mean(axis=0))/s
    else:
        raise Exception("unknown `preprocess`")

    X = X.astype(np.float32, order="C", copy=False) # work with float32

    return X
