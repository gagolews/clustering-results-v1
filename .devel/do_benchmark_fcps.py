"""
Copyright (C) 2023, Marek Gagolewski, https://www.gagolewski.com


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



import rpy2
from rpy2.robjects.packages import importr
import rpy2.robjects.numpy2ri
r_base = importr("base")
#r_base.Sys_setenv(R_LIBS_USER='/home/gagolews/R/x86_64-pc-linux-gnu-library/4.3/')
r_base.source(".devel/do_benchmark_fcps_aux.R")

import numpy as np
import warnings

def do_benchmark_fcps_nonproj(X, Ks):
    #max_K = max(max(Ks), 16)  # just in case we'll need more in the future
    #Ks = list(range(2, max_K+1))
    Ks = np.unique(Ks).tolist()
    res = dict()
    for K in Ks: res[K] = dict()

    rF = rpy2.rinterface.globalenv['fcps_nonproj_apply']
    eX = list(X.astype("double").ravel())
    rX = r_base.matrix(
        rpy2.rinterface.vector(eX, rpy2.rinterface.RTYPES.REALSXP),
        byrow=True, nrow=X.shape[0]
    )

    print(" >:", end="", flush=True)
    for K in Ks:
        rres = rF(data=rX, k=K, verbose=True)
        vres = list(rres)
        nres = list(r_base.names(rres))
        for i in range(len(vres)):
            assert min(vres[i]) == 1
            assert max(vres[i]) == K
            res[K][nres[i]] = vres[i]

        print(":", end="", flush=True)
    print("<", end="", flush=True)
    return res
