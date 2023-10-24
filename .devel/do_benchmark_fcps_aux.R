# Copyright (C) 2023, Marek Gagolewski, https://www.gagolewski.com
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# FCPS 1.3.4 + underlying packages downloaded on 2023-10-21
# install.packages("FCPS", dependencies=TRUE)
suppressPackageStartupMessages(library("FCPS", quietly=TRUE, verbose=FALSE))

set.seed(123)

# We select all algorithms which return an a priori-given number of clusters,
# and do not rely on heavy feature engineering/data projections

# We skip methods that are available in fastcluster and scikit-learn

cases <- list(
    # Affinity propagation (Apclustering) - does not allow k
    # DBSCAN - does not allow k
    # DensityPeakClustering - does not allow k
    # MarkovClustering- does not allow k
    # MSTclustering - does not allow k
    # OPTICSclustering - does not allow k
    # PenalizedRegressionBasedClustering - does not allow k
    # pdfClustering - does not allow k
    # QTclustering - does not allow k
    # SharedNearestNeighborClustering - does not allow k
    # SubspaceClustering - does not allow k

    # AutomaticProjectionBasedClustering - finds a nonlinear projection (different class)
    #list(HierarchicalClustering, "Sparse") # does auto feature selection -> skip (separate class)
    # ProjectionPursuitClustering
    # RobustTrimmedClustering
    # SOMclustering
    # Spectrum - spectral clustering
    # SubspaceClustering - subspaces
    # TandemClustering - combines k-means and PCA

    # CrossEntropyClustering - FCPS documentation mentions that the algorithm is not stable
    # DatabionicSwarmClustering - current implementation is not efficient for N>4000
    # Agglomerative Nesting (AGNES) - this is the ordinary Hierarchical Clustering

    # ModelBasedClustering, MoGclustering - mixture of Gaussians - see scikit-learn

    FCPS_AdaptiveDensityPeak=list(ADPclustering), # default params
    FCPS_Minimax=list(HierarchicalClustering, "Minimax"),  # protoclust::protoclust Minimax Linkage; no params
    FCPS_MinEnergy=list(HierarchicalClustering, "MinEnergy"),  # energy::energy.hclust Hierarchical Clustering by Minimum (Energy) E-distance; MinimalEnergyClustering no params
    FCPS_HDBSCAN_4=list(HierarchicalClustering, "HDBSCAN"), # dbscan::hdbscan HierarchicalDBSCAN minPts=4
    FCPS_HDBSCAN_2=list(HierarchicalClustering, "HDBSCAN", minPts=2),
    FCPS_HDBSCAN_8=list(HierarchicalClustering, "HDBSCAN", minPts=8),
    FCPS_Diana=list(DivisiveAnalysisClustering), # cluster::diana DIvisive ANAlysis Clustering
    FCPS_Fanny=list(FannyClustering, maxit=2000), # cluster::fanny Fuzzy Analysis Clustering
    FCPS_Hardcl=list(HCLclustering), # cclust::cclust(method="hardcl") On-line Update (Hard Competitive learning convex clustering) method
    FCPS_Softcl=list(NeuralGasClustering), # cclust::cclust(method="neuralgas")  Neural Gas (Soft Competitive learning)
    FCPS_Clara=list(LargeApplicationClustering, Standardization=FALSE), # cluster::clara Clustering Large Applications - based on Partitioning Around Medoids on subsets
    FCPS_PAM=list(PAMclustering) #  cluster::pam Partitioning Around Medoids (PAM)
)



fcps_nonproj_apply <- function(data, k, verbose=FALSE)
{
    d <- as.matrix(dist(data))

    res <- list()
    for (i in seq_along(cases)) {
        case <- cases[[i]]

        fun <- case[[1]]
        if ("DataOrDistances" %in% names(formals(fun)))
            args <- list(DataOrDistances=d)
        else
            args <- list(Data=data)

        args <- c(args, ClusterNo=k, case[-1])

        tryCatch({
            y_pred <- as.integer(do.call(fun, args)[["Cls"]])

            .t <- tabulate(y_pred)
            stopifnot(y_pred > 0, length(.t) == k, .t > 0)

            res[[names(cases)[i]]] <- as.integer(y_pred)
            if (verbose) cat(".")
        }, error=function(e) cat("X"))
    }
    res
}
