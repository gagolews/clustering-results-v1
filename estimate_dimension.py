"""
Adapted from Code by Andreas Mueller
https://github.com/amueller/information-theoretic-mst
(licensed under the BSD 2-Clause License)


Copyright (c) 2012, Andreas Mueller All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import numpy as np

from sklearn.neighbors import NearestNeighbors


def estimate_dimension(X, n_neighbors='auto', neighbors_estimator=None):
    """Estimate intrinsic dimensionality.

    Based on "Manifold-Adaptive Dimension Estimation"
    Farahmand, Szepavari, Audibert ICML 2007.

    Parameters
    ----------
    X : nd-array, shape (n_samples, n_features)
        Input data.

    n_neighbors : int or auto, default='auto'
        Number of neighbors used for estimate.
        'auto' means ``np.floor(2 * np.log(n_samples))``.

    neighbors_estimator : NearestNeighbors object or None, default=None
        A pre-fitted neighbors object to speed up calculations.


    Adapted from Code by Andreas Mueller
    https://github.com/amueller/information-theoretic-mst
    (licensed under the BSD 2-Clause License)
    """
    if n_neighbors == 'auto':
        n_neighbors = np.floor(2 * np.log(X.shape[0])).astype("int")

    if neighbors_estimator is None:
        neighbors_estimator = NearestNeighbors(n_neighbors=n_neighbors)
        neighbors_estimator.fit(X)
    full_dist = neighbors_estimator.kneighbors(X, n_neighbors=n_neighbors)[0][:, -1]
    half_dist = neighbors_estimator.kneighbors(X, n_neighbors=n_neighbors // 2)[0][:, -1]



    # Marek's mods:
    est = np.log(2) / (np.log((full_dist  + 1e-16 )/ (half_dist + 1e-16)) + 1e-16)
    est = np.minimum(est, X.shape[1])

    #return np.round(np.mean(est))
    return np.mean(est)
