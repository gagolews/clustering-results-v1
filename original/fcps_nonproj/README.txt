Some algorithms available in the
[`FCPS`](https://cran.r-project.org/package=FCPS) 1.3.4
package for R. The package provides a consistent interface to many other
R packages (versions current as of 2023-10-21).

M.C. Thrun, Q. Stier, Fundamental Clustering Algorithms Suite, SoftwareX 13,
2021, 100642, DOI:10.1016/j.softx.2020.100642.

We selected all algorithms which return an a priori-given number of clusters,
and do not rely on heavy feature engineering/fancy data projections,
as such methods should be evaluated separately.

Note that HDBSCAN might mark certain points as noise (cluster ID of 0).

We did not include the algorithms that are available in other packages and
are already part of this results repository,
e.g., fastcluster, genieclust, and scikit-learn.
