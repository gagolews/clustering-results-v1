#%%silent
#%%restart
#%%cd @


## TODO: This is a draft.
## TODO: This is a draft.
## TODO: This is a draft.






# Copyright (C) 2020, Marek Gagolewski, https://www.gagolewski.com
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



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path, glob, re
#from natsort import natsorted
#import genieclust
import sklearn.metrics
import seaborn as sns
np.set_printoptions(precision=5, threshold=10, edgeitems=10)
pd.set_option("min_rows", 20)
plt.style.use("seaborn-whitegrid")
#plt.rcParams["figure.figsize"] = (8,4)



#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````



# Load results file:
res = pd.read_csv("original/v1-scores.csv")


# ari, afm can be negative --> replace negative indexes with 0.0
res.iloc[:,4:] = res.iloc[:,4:].transform(lambda x: np.maximum(x, 0.0), axis=1)


# I suggest that g2mg, h2mg and all datasets with n>10000 should
# be studied separately.
# Subset: not g2mg, not h2mg
res = res.loc[~res.battery.isin(["g2mg", "h2mg"]), :]

# Subset: [large datasets]
dims = pd.read_csv("original/v1-dims.csv")
res = res.loc[~res.dataset.isin(dims.dataset[dims.n>10_000]), :]


#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````
# Caution: some methods, Birch in particular, might be unable
# to find some K-partitions for given K, therefore it will only be compared
# against reference labels of lower-cardinality  - this puts this algorithm
# at a disadvantage.
#
# Let's first inspect the missing clusterings.
#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````


how_many_labels_true_considered = \
    res.groupby(["battery", "dataset", "method"]).ar.count().\
        unstack(fill_value=0).stack().rename("how_many_labels").reset_index()
num_labels_true = res.loc[:,["battery", "dataset", "labels"]].drop_duplicates().\
    groupby(["battery", "dataset"]).labels.count()


# Number of missing comparisons:
(
    num_labels_true-
    how_many_labels_true_considered.
        set_index(["battery", "dataset", "method"]).iloc[:,0]
).rename("num_missing").reset_index().groupby("method").num_missing.\
    sum().sort_values().reset_index().query("num_missing>0")

# number of complete cases:
(
    ((how_many_labels_true_considered.set_index(["battery", "dataset", "method"]).iloc[:,0]-num_labels_true)==0)
).rename("num_complete").reset_index().groupby("method").num_complete.sum().reset_index()



# number of completely missing cases:
completely_missing = how_many_labels_true_considered.query("how_many_labels == 0").groupby("method").how_many_labels.count().rename("completely_missing").\
    sort_values().reset_index()
completely_missing

# what's missing
_method = "ITM"
_all = pd.Series(res.dataset.unique())
_all[~_all.isin(res.loc[res.method==_method, "dataset"])]


# Subset:
res = res.loc[~res.method.isin(
        completely_missing.query("completely_missing>=10").method.unique()
    ), :]



# TODO: identify missing cases, assign them with scores == 0.0?


#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````
#``````````````````````````````````````````````````````````````````````````````


# For each battery, dataset, method, compute maximal scores across
# all available true (reference) labels (if there alternative labellings
# of a given dataset):
res_max = res.groupby(["battery", "dataset", "method"]).max().\
    reset_index().drop(["labels"], axis=1)
res_max.head()


# np vs. ar vs. ...:
sns.pairplot(res_max.loc[:,["nacc", "psi", "ar", "ami"]])
plt.show()
res_max.loc[:,["nacc", "psi", "ar", "ami"]].describe()


# which similarity measure to report below:
similarity_measure = "ar"

# if we want to colourise the boxes, we'll have to use plt.boxplot()...
__order=res_max.groupby("method")[similarity_measure].median().sort_values().index
plt.rcParams["figure.figsize"] = (8,16)
sns.boxplot(y="method", x=similarity_measure, data=res_max,
            order=__order,
            orient="h",
            showmeans=True,
            meanprops=dict(markeredgecolor="k", marker="x"))
plt.show()


# TODO: indices relative to best index

# TODO: all algorithm groups -> parameter oracle


res_max.groupby("method")[similarity_measure].describe()

res_summary_ar = res_max.groupby(["method"])[similarity_measure].\
    mean().sort_values(ascending=False).rename("mean").\
    reset_index()
print(res_summary_ar)

res_summary_ar = res_max.groupby(["method"])[similarity_measure].\
    median().sort_values(ascending=False).rename("median").\
    reset_index()
print(res_summary_ar)



###############################################################################

# are some test batteries easier than other ones?
test_methods = ['GIc', 'Genie_G0.3', 'Genie_G0.5', 'ITM', 'IcA',
    'sklearn_kmeans', 'sklearn_gm', 'sklearn_spectral_Alaplacian_G5',
    'sklearn_birch_T0.01_BF100', 'fastcluster_ward']
similarity_measure = "psi"
res2 = pd.read_csv("original/v1-scores.csv")
# distinguish datasets with n>10_000:
dims = pd.read_csv("original/v1-dims.csv")
res2.loc[res2.dataset.isin(dims.dataset[dims.n>10_000]),"battery"] = "large"
res2.iloc[:,4:] = res2.iloc[:,4:].transform(lambda x: np.maximum(x, 0.0), axis=1)
res2_max = res2.groupby(["battery", "dataset", "method"]).max().\
    reset_index().drop(["labels"], axis=1)
__data = res2_max.loc[res2_max.method.isin(test_methods),:]
plt.rcParams["figure.figsize"] = (8,16)
sns.boxplot(y="method", x=similarity_measure, hue="battery",
            data=__data,
            orient="h",
            showmeans=True,
            meanprops=dict(markeredgecolor="k", marker="x"))
plt.xlim(-0.2, 1.0)
plt.show()

plt.rcParams["figure.figsize"] = (8,6)
__data_h = __data.groupby(["method","battery"])[similarity_measure].\
    median().unstack()
sns.heatmap(__data_h, annot=True, cmap="YlGnBu")
plt.show()

# "easy"(?) datasets
res2_max.groupby("dataset")[similarity_measure].min().sort_values(ascending=False).head(10)

# "hard" datasets for all the algorithms
res2_max.groupby("dataset")[similarity_measure].max().sort_values().head(10)
