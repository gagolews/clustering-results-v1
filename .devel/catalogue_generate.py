#!/usr/bin/env python3

"""Generates the Catalogue of Clustering Datasets in a Given Directory

Copyleft (C) 2018-2021, Marek Gagolewski <https://www.gagolewski.com>

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


#################################################################################
# Global options

plt.style.use('seaborn-whitegrid')

# Sorry for this being hardcoded!
# See https://github.com/gagolews/clustering_benchmarks_v1/
benchmarks_path = "/home/gagolews/Projects/clustering_benchmarks_v1"

#################################################################################


def process(f, dataset, benchmarks_path, labels_path, output_path):
    """
    Processes a single dataset (yup!).
    """
    X = np.loadtxt(os.path.join(benchmarks_path, dataset+".data.gz"), ndmin=2)
    # X = (X-X.mean(axis=0))/X.std(axis=None, ddof=1) # scale all axes proportionally

    print('# %s (n=%d, d=%d) <a name="%s"></a>\n' % (
        dataset, X.shape[0], X.shape[1], str.replace(dataset, os.path.sep, "_")
    ), file=f)

    fnames = glob.glob(os.path.join(labels_path, dataset) + ".result*.gz")
    Ks = np.unique([int(re.search(r"\.result([0-9]+)\.gz$", fname).group(1))
        for fname in fnames])

    #print(fnames)

    for K in Ks:
        fname = os.path.join(labels_path, dataset) + ".result%d.gz" % K
        labels = pd.read_csv(fname)

        for i in range(labels.shape[1]):
            ll = np.array(labels.iloc[:, i])
            #print("#### `%s`\n\nk=%2d, g=%.3f\n\nlabel_counts=%r\n" % (
                    #labels.columns[i],
                    #max(ll),
                    #genieclust.inequity.gini_index(ll),
                    #np.bincount(ll).tolist()
                #),
                #file=f
            #)

            if X.shape[1] not in [1, 2, 3]:
                print('> **(preview generation suppressed)**\n\n', file=f)
                continue

            plt.figure()
            ax = plt.subplot(111, projection=None if X.shape[1] in [1, 2] else '3d')


            if X.shape[1] == 2:
                genieclust.plots.plot_scatter(X, labels=ll, alpha=0.5)
                plt.axis("equal")

            elif X.shape[1] == 1:
                X_aug = np.insert(X, 1, np.random.randn(len(X))*(X.max()-X.min())*1e-6, axis=1)
                genieclust.plots.plot_scatter(X_aug, labels=ll, alpha=0.5)
                plt.axis("equal")

            elif X.shape[1] == 3:
                ax.scatter(X[:, 0], X[:, 1],
                        c=np.array(genieclust.plots.col, dtype=object)[
                            (ll) % len(genieclust.plots.col)
                        ],
                        alpha=0.5)
                #plt.axis("equal")

            plt.title("%s.%s (n=%d, k=%d)" % (
                dataset,
                labels.columns[i],
                X.shape[0],
                max(ll))
            )

            #_fig_name = "%s.result%d.%s.pdf" % (dataset, K, labels.columns[i])
            #_fig_path = os.path.join(output_path, _fig_name)
            #plt.savefig(_fig_path, format="pdf", transparent=True,
                        #bbox_inches="tight")

            _fig_name = "%s.result%d.%s.png" % (dataset, K, labels.columns[i])
            _fig_path = os.path.join(output_path, _fig_name)
            plt.savefig(_fig_path, format="png", transparent=True,
                        bbox_inches="tight", dpi=72)

            plt.close()

            print("![](%s)" % (_fig_name), file=f)

            # with open(_fig_path, "rb") as img:
                # encoded_string = base64.b64encode(img.read()).decode("US-ASCII")
            #print("<img src='data:image/png;base64,"+encoded_string+"' alt='%s.%s' />\n"%(dataset, label_names[i]), file=f)




    print("\n\n", file=f)


###############################################################################
# Do the job.

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Usage: %s benchmark_folder labels_path output_path" % sys.argv[0])

    folder = sys.argv[1]
    if not os.path.isdir(os.path.join(benchmarks_path, folder)):
        raise Exception("`%s` is not a directory" % folder)

    labels_path = sys.argv[2]
    if not os.path.isdir(labels_path):
        raise Exception("`%s` is not a directory" % labels_path)

    fnames = glob.glob(os.path.join(benchmarks_path, folder, "*.data.gz"))
    datasets = natsorted(
        [re.search("%s[/\\\\]?(.*)\\.data\\.gz" % benchmarks_path, name)[1] for name in fnames])

    output_path = sys.argv[3]
    if not os.path.isdir(output_path): os.mkdir(output_path)

    image_folder = os.path.join(output_path, folder)
    if not os.path.isdir(image_folder): os.mkdir(image_folder)

    output = os.path.join(output_path, "%s.md" % folder)
    f = open(output, "w")


    print("""\
# [Benchmark Suite for Clustering Algorithms - Version 1](https://github.com/gagolews/clustering_benchmarks_v1/) by [Marek Gagolewski](https://www.gagolewski.com) and others

## Results

""", file=f)

    print("**Datasets**\n", file=f)
    for dataset in datasets:
        print("* [%s](#%s)" % (dataset, str.replace(dataset, "/", "_")), file=f)
    print("\n"+("-"*80)+"\n", file=f)

    for dataset in datasets:
        print("Generating %s..." % dataset)
        process(f, dataset, benchmarks_path, labels_path, output_path)
    f.close()

    print("Done.")
