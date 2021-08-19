README
======

This directory and all its subdirectories were generated automatically as
follows. For each dataset, number of clusters K, and cluster validity
measure CVI:

1. fetch all the candidate label vectors and the corresponding CVI values,
2. identify the(a) label vector that yields the greatest CVI,
    using the procedure described in the paper by
    Gagolewski, Bartoszuk, and Cena: 'Are Cluster Validity Measures (In)valid?',
3. store it as a new column in the output CSV file.

Each file is named like 'test_battery/dataset.resultsK.gz', where
K is the number of clusters to detect.

Each file is in a CSV format -- (named) columns give the partitions
with elements in 1..K.
