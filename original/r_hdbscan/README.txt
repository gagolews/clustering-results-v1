dbscan package for R 1.2.7

with different minPts and cluster_selection_epsilon parameters

T <- as.hclust(as.dendrogram(db$hdbscan_tree))
y_pred <- as.integer(cutree(T, k))
