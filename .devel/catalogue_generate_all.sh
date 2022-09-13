#!/bin/bash

# Copyleft (C) 2018-2021, Marek Gagolewski <https://www.gagolewski.com>
# runs ./catalogue_generate.py on a number of test batteries

batteries="fcps graves other sipu uci wut" # mnist h2mg g2mg
labels_path="results_original/other"
output_path="catalogue_original/other"
for b in $batteries; do
    ./catalogue_generate.py $b $labels_path $output_path
    pandoc $output_path/$b.md --to html -o $output_path/$b.html
done
