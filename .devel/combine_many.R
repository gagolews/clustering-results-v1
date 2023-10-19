#!/usr/bin/env Rscript

# Copyleft 2020-2023, Marek Gagolewski <https://www.gagolewski.com>

# combines outputs of many clustering algorithms
# scattered around many sub_paths into one folder output_path


library("stringi")
set.seed(123)






# sorry for the hardcoded paths, but do you really want to run this?


# https://github.com/gagolews/clustering_benchmarks_v1
benchmarks_path <- "~/Projects/clustering_benchmarks_v1"


results_path <- "results_original"

# https://github.com/gagolews/clustering_benchmarks_v1_results
sub_paths <- c(
    "fastcluster_average",
    "fastcluster_centroid",
    "fastcluster_complete",
    "fastcluster_median",
    "fastcluster_ward",
    "fastcluster_weighted",
    "Genie",
    "GIc",
    "IcA",
    "ITM",
#     "sklearn_birch",  # too many params
#     "sklearn_spectral",  # too many params
    "sklearn_kmeans",
    "sklearn_gm"
)

output_path <- "results_original/other"



# sub_paths <- list.dirs(results_path, full.names=FALSE, recursive=FALSE)








load_dataset <- function(dataset, benchmarks_path) {
    data_file <- file.path(benchmarks_path, paste0(dataset, ".data.gz"))
    X    <- read.table(data_file)
    X <- X[, apply(X, 2, var) > 0, drop=FALSE] # remove all columns of 0 variance
    n <- nrow(X)
    d <- ncol(X)

    # add a tiny bit of random noise, center and scale
    X <- t(X)
    X[,] <- X + rnorm(n*d, 0, apply(X, 1, sd)*1e-6)
    X[,] <- X - apply(X, 1, mean)
    X[,] <- X / sd(X) # this is not standardisation
    X <- t(X)

    X
}


load_true_labels <- function(dataset, benchmarks_path) {
    path <- file.path(benchmarks_path, sprintf("%s.labels*.gz", dataset))
    files <- list.files(dirname(path),
        glob2rx(basename(path)),
        recursive=TRUE,
        full.names=TRUE)
    all_labels <- lapply(files, read.table)
    Y <- as.matrix(do.call(cbind, all_labels))
    dimnames(Y) <- list(NULL, paste0("labels", 0:(ncol(Y)-1)))
    Y
}


load_pred_labels <- function(dataset, results_path, sub_path, K) {
    path <- file.path(results_path, sub_path,
        sprintf("%s.result%d.gz", dataset, K))
    if (file.exists(path)) {
        as.matrix(read.csv(path))
    } else {
        cat(sprintf("file does not exist: %s\n", path))
        NULL
    }
}


merge_noise_points_with_nearest_clusters <- function(y, X) {
    stopifnot(length(y) == nrow(X))

    wh_noise <- which(y == 0)
    if (length(wh_noise) == 0) return(y)

    nns <- FNN::get.knnx(X[-wh_noise, , drop=FALSE],
                         X[ wh_noise, , drop=FALSE], 1)$nn.index
    y[wh_noise] <- y[-wh_noise][nns]

    y
}


crossprintf <- function(fmt, ...) {
    args <- c(rev(list(...)), stringsAsFactors=FALSE)
    x <- rev(do.call(expand.grid, args))
    sapply(seq_len(nrow(x)), function(i)
        do.call(sprintf, c(fmt, x[i, , drop=FALSE])))
}






datasets <- stri_sub(list.files(benchmarks_path, glob2rx("*.data.gz"),
    full.names=FALSE, recursive=TRUE), to=-9)

for (dataset in datasets) {

    X <- load_dataset(dataset, benchmarks_path)
    n <- nrow(X)
    d <- ncol(X)

    Y_true <- load_true_labels(dataset, benchmarks_path)
    #Y_true <- apply(Y_true, 2, merge_noise_points_with_nearest_clusters, X)
    Ks <- apply(Y_true, 2, max)

    for (K in unique(Ks)) {
        cat(sprintf("%20s: n=%6d, d=%3d, K=%3d\n", dataset, n, d, K))

        out_fname <- file.path(output_path,
            sprintf("%s.result%d.gz", dataset, K))
        if (!dir.exists(dirname(out_fname)))
            dir.create(dirname(out_fname))

        if (file.exists(out_fname)) next

        Y_start <- do.call(cbind, lapply(sub_paths, function(sub_path)
            load_pred_labels(dataset, results_path, sub_path, K)))

        Y_start <- cbind(Y_true[, K==Ks, drop=FALSE], Y_start)

#         stopifnot(apply(Y_start, 2, min)==1)
        stopifnot(apply(Y_start, 2, max)==K)

        f <- gzfile(out_fname, "w")
        write.csv(Y_start, f, row.names=FALSE)
        close(f)
        rm(f)
    }
}
