#!/usr/bin/env python3

"""Generates the Catalogue of Clustering Results

Copyleft (C) 2018-2023, Marek Gagolewski <https://www.gagolewski.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import os
import glob
import re
import sys
import genieclust
from natsort import natsorted
import shutil
import clustbench

# TODO: git-filter-repo --path .catalogue/original --invert-paths --force

#################################################################################
# Global options

# Sorry for this being hardcoded!
# See https://github.com/gagolews/clustering-data-v1/
data_path = os.path.expanduser("~/Projects/clustering-data-v1")
# See https://github.com/gagolews/clustering-results-v1/
results_path = os.path.expanduser("~/Projects/clustering-results-v1/original")

ignore_methods_regex = r".*DuNN_.*|^sklearn_birch.*|^sklearn_spectral.*" + \
    "|.*WCNN.*|^Test_.*|^mst_.*"

include_methods = [
    "sklearn_birch_T0.01_BF50",
    "sklearn_spectral_Alaplacian_G5",
    "DuNN_25_Min_Max",
    "DuNN_25_Mean_Mean",
    "DuNN_25_Max_Min",
    "WCNN_25",
    "mst_divisive_BallHall","mst_divisive_CalinskiHarabasz","mst_divisive_DaviesBouldin","mst_divisive_Silhouette","mst_divisive_SilhouetteW","mst_divisive_GDunn_d1_D1","mst_divisive_GDunn_d1_D2","mst_divisive_GDunn_d1_D3","mst_divisive_GDunn_d2_D1","mst_divisive_GDunn_d2_D2","mst_divisive_GDunn_d2_D3","mst_divisive_GDunn_d3_D1","mst_divisive_GDunn_d3_D2","mst_divisive_GDunn_d3_D3","mst_divisive_GDunn_d4_D1","mst_divisive_GDunn_d4_D2","mst_divisive_GDunn_d4_D3","mst_divisive_GDunn_d5_D1","mst_divisive_GDunn_d5_D2","mst_divisive_GDunn_d5_D3",
    "mst_divisive_DuNN_25_Min_Max",
    "mst_divisive_DuNN_25_Mean_Mean",
    "mst_divisive_DuNN_25_Max_Min",
    "mst_divisive_WCNN_25",
]

plt.style.use("seaborn-v0_8-whitegrid")  # overall plot style

_colours = [  # the "R4" palette
    "#000000", "#DF536B", "#61D04F", "#2297E6",
    "#28E2E5", "#CD0BBC", "#F5C710", "#999999"
]

_linestyles = [
    "solid", "dashed", "dashdot", "dotted"
]

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    # each plotted line will have a different plotting style
    color=_colours, linestyle=_linestyles*2
)
plt.rcParams["patch.facecolor"] = _colours[0]

np.random.seed(123)  # initialise the pseudorandom number generator

plt.rcParams.update({  # further graphical parameters
    "font.size":         13,
    "font.family":       "sans-serif",
    "font.sans-serif":   ["Alegreya Sans", "Alegreya"],
    "figure.autolayout": True,
    "figure.dpi":        96,
    "figure.figsize":    (3.5, 3.5),
})


#################################################################################



# TODO: rewrite using clustbench.load_dataset etc.

def process(f, battery, dataset):
    """
    Processes a single dataset
    """
    b = clustbench.load_dataset(battery, dataset, path=data_path, preprocess=False)
    X = b.data

    print('## %s/%s (n=%d, d=%d) <a name="%s"></a>\n' % (
        battery, dataset, X.shape[0], X.shape[1], dataset
    ), file=f)

    labels = b.labels
    label_names = [("labels%d" % i) for i in range(len(labels))]
    true_K = [max(ll) for ll in labels]
    all_K = np.unique(true_K)

    if X.shape[1] not in [1, 2, 3]:
        print('> **(preview generation suppressed)**\n\n', file=f)

    res = []
    results = clustbench.load_results("*", battery, dataset, all_K, results_path)

    scores = dict()
    for method in results.keys():
        scores[method] = clustbench.get_score(labels, results[method])
    scores = pd.Series(scores).sort_values(ascending=False)

    for method in scores.index:
        if (re.search(ignore_methods_regex, method) is not None) and (method not in include_methods):
            continue

        print('#### %s (NCA=%.2f)\n' % (method, scores[method]), file=f)

        for k in all_K:
            if k not in results[method]:
                continue

            res.append(dict(
                battery=battery,
                dataset=dataset,
                k=k,
                method=method
            ))

            if X.shape[1] not in [1, 2, 3]:
                #print('> **(preview generation suppressed)**\n\n', file=f)
                continue

            plt.figure()
            ax = plt.subplot(111, projection=None if X.shape[1] in [1, 2] else '3d')


            if X.shape[1] == 2:
                genieclust.plots.plot_scatter(X, labels=results[method][k]-1, alpha=0.5)
                plt.axis("equal")

            elif X.shape[1] == 1:
                X_aug = np.insert(X, 1, np.random.randn(len(X))*(X.max()-X.min())*1e-6, axis=1)
                genieclust.plots.plot_scatter(X_aug, labels=results[method][k]-1, alpha=0.5)
                plt.axis("equal")

            elif X.shape[1] == 3:
                ax.scatter(
                    X[:, 0],
                    X[:, 1],
                    c=np.array(genieclust.plots.col, dtype=object)[
                        (results[method][k]-1) % len(genieclust.plots.col)
                    ],
                    alpha=0.5
                )
                #plt.axis("equal")

            plt.title("%s/%s (n=%d, k=%d)\n%s" % (
                battery,
                dataset,
                X.shape[0],
                k,
                method
            ))

            _fig_name = os.path.join(battery, "%s.result%d.%s.jpg" % (dataset, k, method))
            _fig_path = os.path.join(".catalogue", "original", _fig_name)
            plt.savefig(_fig_path, format='jpg',
                        #transparent=True,
                        bbox_inches='tight',
                        #dpi=150
            )
            plt.close()

            print("![](%s)" % (_fig_name), file=f)

        # end for each k
        print("\n\n", file=f)
    # end for each method

    return res


###############################################################################
# Do the job.

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: %s benchmark_folder" % sys.argv[0])

    battery = sys.argv[1]

    #fnames = glob.glob("*.data.gz", root_dir=battery)
    datasets = clustbench.get_dataset_names(battery, data_path)

    image_folder = os.path.join(".catalogue", "original", battery)
    if not os.path.isdir(image_folder): os.mkdir(image_folder)

    output = os.path.join(".catalogue", "original", "%s.md" % battery)
    f = open(output, "w")

    print("The **[Framework for Benchmarking Clustering Algorithms](https://clustering-benchmarks.gagolewski.com)", file=f)
    print("is authored/edited/maintained by [Marek Gagolewski](https://www.gagolewski.com)**\n", file=f)

    with np.DataSource().open(os.path.join(data_path, "VERSION")) as vf:
        version = vf.read()

    print("\n[Benchmark suite](https://github.com/gagolews/clustering-data-v1) version %s\n" % version, file=f)

    print("\n"+("-"*80)+"\n", file=f)

    print("**Datasets**\n", file=f)
    for dataset in datasets:
        print("* [%s/%s](#%s)" % (
            battery, dataset, dataset
        ), file=f)

    print('\n\n*(results are sorted wrt the normalised clustering accuracy score – comparison against the reference labels; see the Framework\'s [homepage](https://clustering-benchmarks.gagolewski.com) for more details)*\n\n', file=f)

    print("\n"+("-"*80)+"\n", file=f)

    metadata = []
    for dataset in datasets:
        print("Generating %s/%s... " % (battery, dataset), end="")
        metadata += process(f, battery, dataset)
        print("")
    f.close()

    metadata_file = os.path.join(".catalogue", "original", "%s.csv" % battery)
    pd.DataFrame(metadata).\
        loc[:, ["battery", "dataset", "k", "method"]].\
        to_csv(metadata_file, header=True, index=False)

    print("Done.")
