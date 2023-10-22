The **[Framework for Benchmarking Clustering Algorithms](https://clustering-benchmarks.gagolewski.com)
is authored/edited/maintained by [Marek Gagolewski](https://www.gagolewski.com)**


[Benchmark suite](https://github.com/gagolews/clustering-data-v1) version 1.1.0



--------------------------------------------------------------------------------

**Datasets**

* [sipu/a1](#a1)
* [sipu/a2](#a2)
* [sipu/a3](#a3)
* [sipu/aggregation](#aggregation)
* [sipu/birch1](#birch1)
* [sipu/birch2](#birch2)
* [sipu/compound](#compound)
* [sipu/d31](#d31)
* [sipu/flame](#flame)
* [sipu/jain](#jain)
* [sipu/pathbased](#pathbased)
* [sipu/r15](#r15)
* [sipu/s1](#s1)
* [sipu/s2](#s2)
* [sipu/s3](#s3)
* [sipu/s4](#s4)
* [sipu/spiral](#spiral)
* [sipu/unbalance](#unbalance)
* [sipu/worms_2](#worms_2)
* [sipu/worms_64](#worms_64)


*(results are sorted wrt the normalised clustering accuracy score – comparison against the reference labels; see the Framework's [homepage](https://clustering-benchmarks.gagolewski.com) for more details)*



--------------------------------------------------------------------------------

## sipu/a1 (n=3000, d=2) <a name="a1"></a>

#### FCPS_Softcl (NCA=0.98)

![](sipu/a1.result20.FCPS_Softcl.jpg)



#### FCPS_Fanny (NCA=0.98)

![](sipu/a1.result20.FCPS_Fanny.jpg)



#### sklearn_kmeans (NCA=0.98)

![](sipu/a1.result20.sklearn_kmeans.jpg)



#### FCPS_PAM (NCA=0.98)

![](sipu/a1.result20.FCPS_PAM.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.98)

![](sipu/a1.result20.sklearn_spectral_Alaplacian_G5.jpg)



#### sklearn_gm (NCA=0.98)

![](sipu/a1.result20.sklearn_gm.jpg)



#### FCPS_Clara (NCA=0.97)

![](sipu/a1.result20.FCPS_Clara.jpg)



#### CTCEHC (NCA=0.97)

![](sipu/a1.result20.CTCEHC.jpg)



#### GIc (NCA=0.97)

![](sipu/a1.result20.GIc.jpg)



#### Genie_G0.1 (NCA=0.97)

![](sipu/a1.result20.Genie_G0.1.jpg)



#### fastcluster_centroid (NCA=0.97)

![](sipu/a1.result20.fastcluster_centroid.jpg)



#### mst_divisive_BallHall (NCA=0.96)

![](sipu/a1.result20.mst_divisive_BallHall.jpg)



#### mst_divisive_Silhouette (NCA=0.96)

![](sipu/a1.result20.mst_divisive_Silhouette.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.96)

![](sipu/a1.result20.sklearn_birch_T0.01_BF50.jpg)



#### fastcluster_average (NCA=0.96)

![](sipu/a1.result20.fastcluster_average.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.96)

![](sipu/a1.result20.mst_divisive_CalinskiHarabasz.jpg)



#### FCPS_MinEnergy (NCA=0.96)

![](sipu/a1.result20.FCPS_MinEnergy.jpg)



#### fastcluster_complete (NCA=0.96)

![](sipu/a1.result20.fastcluster_complete.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.95)

![](sipu/a1.result20.FCPS_AdaptiveDensityPeak.jpg)



#### fastcluster_ward (NCA=0.95)

![](sipu/a1.result20.fastcluster_ward.jpg)



#### FCPS_Minimax (NCA=0.94)

![](sipu/a1.result20.FCPS_Minimax.jpg)



#### mst_divisive_WCNN_25 (NCA=0.91)

![](sipu/a1.result20.mst_divisive_WCNN_25.jpg)



#### Genie_G0.3 (NCA=0.91)

![](sipu/a1.result20.Genie_G0.3.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.91)

![](sipu/a1.result20.mst_divisive_DuNN_25_Min_Max.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.91)

![](sipu/a1.result20.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### FCPS_Diana (NCA=0.91)

![](sipu/a1.result20.FCPS_Diana.jpg)



#### fastcluster_weighted (NCA=0.87)

![](sipu/a1.result20.fastcluster_weighted.jpg)



#### Genie_G0.5 (NCA=0.84)

![](sipu/a1.result20.Genie_G0.5.jpg)



#### fastcluster_median (NCA=0.83)

![](sipu/a1.result20.fastcluster_median.jpg)



#### IcA (NCA=0.83)

![](sipu/a1.result20.IcA.jpg)



#### ITM (NCA=0.82)

![](sipu/a1.result20.ITM.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.72)

![](sipu/a1.result20.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.70)

![](sipu/a1.result20.mst_divisive_GDunn_d2_D2.jpg)



#### HEMST (NCA=0.70)

![](sipu/a1.result20.HEMST.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.68)

![](sipu/a1.result20.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.67)

![](sipu/a1.result20.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.65)

![](sipu/a1.result20.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.65)

![](sipu/a1.result20.mst_divisive_GDunn_d5_D3.jpg)



#### FCPS_Hardcl (NCA=0.62)

![](sipu/a1.result20.FCPS_Hardcl.jpg)



#### Genie_G0.7 (NCA=0.58)

![](sipu/a1.result20.Genie_G0.7.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.50)

![](sipu/a1.result20.mst_divisive_DuNN_25_Max_Min.jpg)



#### Genie_G1.0 (NCA=0.37)

![](sipu/a1.result20.Genie_G1.0.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.37)

![](sipu/a1.result20.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.37)

![](sipu/a1.result20.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.37)

![](sipu/a1.result20.mst_divisive_GDunn_d1_D1.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.37)

![](sipu/a1.result20.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.32)

![](sipu/a1.result20.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.32)

![](sipu/a1.result20.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.30)

![](sipu/a1.result20.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.30)

![](sipu/a1.result20.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.24)

![](sipu/a1.result20.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.22)

![](sipu/a1.result20.mst_divisive_GDunn_d4_D1.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.16)

![](sipu/a1.result20.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.06)

![](sipu/a1.result20.mst_divisive_DaviesBouldin.jpg)



#### mst_divisive_SilhouetteW (NCA=0.01)

![](sipu/a1.result20.mst_divisive_SilhouetteW.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.00)

![](sipu/a1.result20.FCPS_HDBSCAN_8.jpg)



## sipu/a2 (n=5250, d=2) <a name="a2"></a>

#### sklearn_kmeans (NCA=0.98)

![](sipu/a2.result35.sklearn_kmeans.jpg)



#### FCPS_PAM (NCA=0.98)

![](sipu/a2.result35.FCPS_PAM.jpg)



#### sklearn_gm (NCA=0.98)

![](sipu/a2.result35.sklearn_gm.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.98)

![](sipu/a2.result35.sklearn_spectral_Alaplacian_G5.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.98)

![](sipu/a2.result35.FCPS_AdaptiveDensityPeak.jpg)



#### Genie_G0.1 (NCA=0.97)

![](sipu/a2.result35.Genie_G0.1.jpg)



#### GIc (NCA=0.97)

![](sipu/a2.result35.GIc.jpg)



#### CTCEHC (NCA=0.97)

![](sipu/a2.result35.CTCEHC.jpg)



#### fastcluster_centroid (NCA=0.97)

![](sipu/a2.result35.fastcluster_centroid.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.97)

![](sipu/a2.result35.sklearn_birch_T0.01_BF50.jpg)



#### fastcluster_average (NCA=0.97)

![](sipu/a2.result35.fastcluster_average.jpg)



#### FCPS_MinEnergy (NCA=0.96)

![](sipu/a2.result35.FCPS_MinEnergy.jpg)



#### fastcluster_ward (NCA=0.96)

![](sipu/a2.result35.fastcluster_ward.jpg)



#### FCPS_Minimax (NCA=0.96)

![](sipu/a2.result35.FCPS_Minimax.jpg)



#### fastcluster_complete (NCA=0.95)

![](sipu/a2.result35.fastcluster_complete.jpg)



#### FCPS_Softcl (NCA=0.95)

![](sipu/a2.result35.FCPS_Softcl.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.95)

![](sipu/a2.result35.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_WCNN_25 (NCA=0.94)

![](sipu/a2.result35.mst_divisive_WCNN_25.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.94)

![](sipu/a2.result35.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### Genie_G0.3 (NCA=0.94)

![](sipu/a2.result35.Genie_G0.3.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.94)

![](sipu/a2.result35.mst_divisive_DuNN_25_Min_Max.jpg)



#### mst_divisive_BallHall (NCA=0.94)

![](sipu/a2.result35.mst_divisive_BallHall.jpg)



#### FCPS_Clara (NCA=0.93)

![](sipu/a2.result35.FCPS_Clara.jpg)



#### mst_divisive_Silhouette (NCA=0.93)

![](sipu/a2.result35.mst_divisive_Silhouette.jpg)



#### fastcluster_weighted (NCA=0.90)

![](sipu/a2.result35.fastcluster_weighted.jpg)



#### fastcluster_median (NCA=0.88)

![](sipu/a2.result35.fastcluster_median.jpg)



#### Genie_G0.5 (NCA=0.83)

![](sipu/a2.result35.Genie_G0.5.jpg)



#### ITM (NCA=0.83)

![](sipu/a2.result35.ITM.jpg)



#### FCPS_Diana (NCA=0.82)

![](sipu/a2.result35.FCPS_Diana.jpg)



#### FCPS_Hardcl (NCA=0.82)

![](sipu/a2.result35.FCPS_Hardcl.jpg)



#### IcA (NCA=0.80)

![](sipu/a2.result35.IcA.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.72)

![](sipu/a2.result35.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.69)

![](sipu/a2.result35.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.67)

![](sipu/a2.result35.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.66)

![](sipu/a2.result35.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.64)

![](sipu/a2.result35.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.64)

![](sipu/a2.result35.mst_divisive_GDunn_d5_D3.jpg)



#### HEMST (NCA=0.59)

![](sipu/a2.result35.HEMST.jpg)



#### Genie_G0.7 (NCA=0.56)

![](sipu/a2.result35.Genie_G0.7.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.45)

![](sipu/a2.result35.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.38)

![](sipu/a2.result35.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.35)

![](sipu/a2.result35.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.33)

![](sipu/a2.result35.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.33)

![](sipu/a2.result35.mst_divisive_GDunn_d1_D3.jpg)



#### Genie_G1.0 (NCA=0.30)

![](sipu/a2.result35.Genie_G1.0.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.30)

![](sipu/a2.result35.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.29)

![](sipu/a2.result35.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.25)

![](sipu/a2.result35.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.25)

![](sipu/a2.result35.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.23)

![](sipu/a2.result35.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.22)

![](sipu/a2.result35.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.17)

![](sipu/a2.result35.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.15)

![](sipu/a2.result35.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_SilhouetteW (NCA=0.01)

![](sipu/a2.result35.mst_divisive_SilhouetteW.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.00)

![](sipu/a2.result35.FCPS_HDBSCAN_8.jpg)



## sipu/a3 (n=7500, d=2) <a name="a3"></a>

#### FCPS_AdaptiveDensityPeak (NCA=0.99)

![](sipu/a3.result50.FCPS_AdaptiveDensityPeak.jpg)



#### FCPS_PAM (NCA=0.98)

![](sipu/a3.result50.FCPS_PAM.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.98)

![](sipu/a3.result50.sklearn_spectral_Alaplacian_G5.jpg)



#### Genie_G0.1 (NCA=0.98)

![](sipu/a3.result50.Genie_G0.1.jpg)



#### GIc (NCA=0.98)

![](sipu/a3.result50.GIc.jpg)



#### CTCEHC (NCA=0.97)

![](sipu/a3.result50.CTCEHC.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.97)

![](sipu/a3.result50.sklearn_birch_T0.01_BF50.jpg)



#### FCPS_MinEnergy (NCA=0.97)

![](sipu/a3.result50.FCPS_MinEnergy.jpg)



#### fastcluster_average (NCA=0.97)

![](sipu/a3.result50.fastcluster_average.jpg)



#### mst_divisive_Silhouette (NCA=0.97)

![](sipu/a3.result50.mst_divisive_Silhouette.jpg)



#### fastcluster_ward (NCA=0.97)

![](sipu/a3.result50.fastcluster_ward.jpg)



#### sklearn_gm (NCA=0.96)

![](sipu/a3.result50.sklearn_gm.jpg)



#### sklearn_kmeans (NCA=0.96)

![](sipu/a3.result50.sklearn_kmeans.jpg)



#### FCPS_Softcl (NCA=0.96)

![](sipu/a3.result50.FCPS_Softcl.jpg)



#### mst_divisive_WCNN_25 (NCA=0.96)

![](sipu/a3.result50.mst_divisive_WCNN_25.jpg)



#### fastcluster_centroid (NCA=0.96)

![](sipu/a3.result50.fastcluster_centroid.jpg)



#### fastcluster_complete (NCA=0.96)

![](sipu/a3.result50.fastcluster_complete.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.96)

![](sipu/a3.result50.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### Genie_G0.3 (NCA=0.95)

![](sipu/a3.result50.Genie_G0.3.jpg)



#### FCPS_Minimax (NCA=0.94)

![](sipu/a3.result50.FCPS_Minimax.jpg)



#### FCPS_Clara (NCA=0.94)

![](sipu/a3.result50.FCPS_Clara.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.93)

![](sipu/a3.result50.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.93)

![](sipu/a3.result50.mst_divisive_DuNN_25_Min_Max.jpg)



#### fastcluster_weighted (NCA=0.90)

![](sipu/a3.result50.fastcluster_weighted.jpg)



#### fastcluster_median (NCA=0.87)

![](sipu/a3.result50.fastcluster_median.jpg)



#### Genie_G0.5 (NCA=0.84)

![](sipu/a3.result50.Genie_G0.5.jpg)



#### ITM (NCA=0.83)

![](sipu/a3.result50.ITM.jpg)



#### FCPS_Diana (NCA=0.82)

![](sipu/a3.result50.FCPS_Diana.jpg)



#### FCPS_Hardcl (NCA=0.81)

![](sipu/a3.result50.FCPS_Hardcl.jpg)



#### IcA (NCA=0.76)

![](sipu/a3.result50.IcA.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.71)

![](sipu/a3.result50.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.70)

![](sipu/a3.result50.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.66)

![](sipu/a3.result50.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.65)

![](sipu/a3.result50.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.64)

![](sipu/a3.result50.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.63)

![](sipu/a3.result50.mst_divisive_GDunn_d5_D2.jpg)



#### HEMST (NCA=0.63)

![](sipu/a3.result50.HEMST.jpg)



#### Genie_G0.7 (NCA=0.59)

![](sipu/a3.result50.Genie_G0.7.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.51)

![](sipu/a3.result50.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_BallHall (NCA=0.39)

![](sipu/a3.result50.mst_divisive_BallHall.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.31)

![](sipu/a3.result50.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.30)

![](sipu/a3.result50.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.28)

![](sipu/a3.result50.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.26)

![](sipu/a3.result50.mst_divisive_GDunn_d3_D2.jpg)



#### Genie_G1.0 (NCA=0.25)

![](sipu/a3.result50.Genie_G1.0.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.25)

![](sipu/a3.result50.mst_divisive_GDunn_d1_D2.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.25)

![](sipu/a3.result50.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.25)

![](sipu/a3.result50.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.14)

![](sipu/a3.result50.mst_divisive_GDunn_d4_D1.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.13)

![](sipu/a3.result50.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.10)

![](sipu/a3.result50.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.10)

![](sipu/a3.result50.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.07)

![](sipu/a3.result50.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.02)

![](sipu/a3.result50.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_SilhouetteW (NCA=0.01)

![](sipu/a3.result50.mst_divisive_SilhouetteW.jpg)



## sipu/aggregation (n=788, d=2) <a name="aggregation"></a>

#### fastcluster_average (NCA=1.00)

![](sipu/aggregation.result7.fastcluster_average.jpg)



#### sklearn_gm (NCA=1.00)

![](sipu/aggregation.result7.sklearn_gm.jpg)



#### WCNN_25 (NCA=1.00)

![](sipu/aggregation.result7.WCNN_25.jpg)



#### BallHall (NCA=1.00)

![](sipu/aggregation.result7.BallHall.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/aggregation.result7.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=1.00)

![](sipu/aggregation.result7.sklearn_spectral_Alaplacian_G5.jpg)



#### mst_divisive_WCNN_25 (NCA=1.00)

![](sipu/aggregation.result7.mst_divisive_WCNN_25.jpg)



#### fastcluster_centroid (NCA=1.00)

![](sipu/aggregation.result7.fastcluster_centroid.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.96)

![](sipu/aggregation.result7.FCPS_AdaptiveDensityPeak.jpg)



#### DaviesBouldin (NCA=0.96)

![](sipu/aggregation.result7.DaviesBouldin.jpg)



#### mst_divisive_Silhouette (NCA=0.96)

![](sipu/aggregation.result7.mst_divisive_Silhouette.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.94)

![](sipu/aggregation.result7.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_BallHall (NCA=0.94)

![](sipu/aggregation.result7.mst_divisive_BallHall.jpg)



#### GDunn_d3_D2 (NCA=0.93)

![](sipu/aggregation.result7.GDunn_d3_D2.jpg)



#### GDunn_d4_D3 (NCA=0.92)

![](sipu/aggregation.result7.GDunn_d4_D3.jpg)



#### GDunn_d4_D1 (NCA=0.92)

![](sipu/aggregation.result7.GDunn_d4_D1.jpg)



#### GDunn_d4_D2 (NCA=0.92)

![](sipu/aggregation.result7.GDunn_d4_D2.jpg)



#### GDunn_d2_D1 (NCA=0.90)

![](sipu/aggregation.result7.GDunn_d2_D1.jpg)



#### GDunn_d2_D3 (NCA=0.90)

![](sipu/aggregation.result7.GDunn_d2_D3.jpg)



#### GDunn_d3_D3 (NCA=0.90)

![](sipu/aggregation.result7.GDunn_d3_D3.jpg)



#### GDunn_d3_D1 (NCA=0.90)

![](sipu/aggregation.result7.GDunn_d3_D1.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.89)

![](sipu/aggregation.result7.mst_divisive_DuNN_25_Min_Max.jpg)



#### Genie_G0.5 (NCA=0.88)

![](sipu/aggregation.result7.Genie_G0.5.jpg)



#### DuNN_25_Min_Max (NCA=0.87)

![](sipu/aggregation.result7.DuNN_25_Min_Max.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.85)

![](sipu/aggregation.result7.mst_divisive_GDunn_d3_D2.jpg)



#### Silhouette (NCA=0.82)

![](sipu/aggregation.result7.Silhouette.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.81)

![](sipu/aggregation.result7.mst_divisive_GDunn_d3_D3.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.78)

![](sipu/aggregation.result7.sklearn_birch_T0.01_BF50.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.78)

![](sipu/aggregation.result7.mst_divisive_GDunn_d3_D1.jpg)



#### fastcluster_ward (NCA=0.78)

![](sipu/aggregation.result7.fastcluster_ward.jpg)



#### GDunn_d2_D2 (NCA=0.78)

![](sipu/aggregation.result7.GDunn_d2_D2.jpg)



#### FCPS_Diana (NCA=0.77)

![](sipu/aggregation.result7.FCPS_Diana.jpg)



#### FCPS_MinEnergy (NCA=0.76)

![](sipu/aggregation.result7.FCPS_MinEnergy.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.75)

![](sipu/aggregation.result7.mst_divisive_GDunn_d4_D2.jpg)



#### fastcluster_complete (NCA=0.75)

![](sipu/aggregation.result7.fastcluster_complete.jpg)



#### CalinskiHarabasz (NCA=0.75)

![](sipu/aggregation.result7.CalinskiHarabasz.jpg)



#### sklearn_kmeans (NCA=0.75)

![](sipu/aggregation.result7.sklearn_kmeans.jpg)



#### fastcluster_weighted (NCA=0.75)

![](sipu/aggregation.result7.fastcluster_weighted.jpg)



#### FCPS_PAM (NCA=0.74)

![](sipu/aggregation.result7.FCPS_PAM.jpg)



#### FCPS_Clara (NCA=0.74)

![](sipu/aggregation.result7.FCPS_Clara.jpg)



#### fastcluster_median (NCA=0.72)

![](sipu/aggregation.result7.fastcluster_median.jpg)



#### FCPS_Softcl (NCA=0.71)

![](sipu/aggregation.result7.FCPS_Softcl.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.69)

![](sipu/aggregation.result7.mst_divisive_GDunn_d4_D3.jpg)



#### IcA (NCA=0.68)

![](sipu/aggregation.result7.IcA.jpg)



#### FCPS_Minimax (NCA=0.68)

![](sipu/aggregation.result7.FCPS_Minimax.jpg)



#### HEMST (NCA=0.67)

![](sipu/aggregation.result7.HEMST.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.66)

![](sipu/aggregation.result7.FCPS_HDBSCAN_4.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.66)

![](sipu/aggregation.result7.FCPS_HDBSCAN_8.jpg)



#### Genie_G1.0 (NCA=0.66)

![](sipu/aggregation.result7.Genie_G1.0.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.66)

![](sipu/aggregation.result7.mst_divisive_GDunn_d1_D3.jpg)



#### GDunn_d1_D3 (NCA=0.66)

![](sipu/aggregation.result7.GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.66)

![](sipu/aggregation.result7.mst_divisive_GDunn_d1_D2.jpg)



#### GDunn_d1_D1 (NCA=0.66)

![](sipu/aggregation.result7.GDunn_d1_D1.jpg)



#### GDunn_d1_D2 (NCA=0.66)

![](sipu/aggregation.result7.GDunn_d1_D2.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.66)

![](sipu/aggregation.result7.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.66)

![](sipu/aggregation.result7.mst_divisive_GDunn_d1_D1.jpg)



#### ITM (NCA=0.66)

![](sipu/aggregation.result7.ITM.jpg)



#### CTCEHC (NCA=0.66)

![](sipu/aggregation.result7.CTCEHC.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.66)

![](sipu/aggregation.result7.mst_divisive_GDunn_d4_D1.jpg)



#### Genie_G0.7 (NCA=0.64)

![](sipu/aggregation.result7.Genie_G0.7.jpg)



#### GIc (NCA=0.64)

![](sipu/aggregation.result7.GIc.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.64)

![](sipu/aggregation.result7.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.63)

![](sipu/aggregation.result7.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.62)

![](sipu/aggregation.result7.mst_divisive_DuNN_25_Max_Min.jpg)



#### FCPS_Fanny (NCA=0.62)

![](sipu/aggregation.result7.FCPS_Fanny.jpg)



#### Genie_G0.1 (NCA=0.58)

![](sipu/aggregation.result7.Genie_G0.1.jpg)



#### Genie_G0.3 (NCA=0.58)

![](sipu/aggregation.result7.Genie_G0.3.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.57)

![](sipu/aggregation.result7.mst_divisive_GDunn_d2_D1.jpg)



#### FCPS_Hardcl (NCA=0.56)

![](sipu/aggregation.result7.FCPS_Hardcl.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.50)

![](sipu/aggregation.result7.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.50)

![](sipu/aggregation.result7.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.49)

![](sipu/aggregation.result7.mst_divisive_GDunn_d2_D3.jpg)



#### GDunn_d5_D2 (NCA=0.37)

![](sipu/aggregation.result7.GDunn_d5_D2.jpg)



#### DuNN_25_Max_Min (NCA=0.37)

![](sipu/aggregation.result7.DuNN_25_Max_Min.jpg)



#### GDunn_d5_D1 (NCA=0.23)

![](sipu/aggregation.result7.GDunn_d5_D1.jpg)



#### GDunn_d5_D3 (NCA=0.05)

![](sipu/aggregation.result7.GDunn_d5_D3.jpg)



#### DuNN_25_Mean_Mean (NCA=0.04)

![](sipu/aggregation.result7.DuNN_25_Mean_Mean.jpg)



#### SilhouetteW (NCA=0.03)

![](sipu/aggregation.result7.SilhouetteW.jpg)



#### mst_divisive_SilhouetteW (NCA=0.01)

![](sipu/aggregation.result7.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.01)

![](sipu/aggregation.result7.mst_divisive_DaviesBouldin.jpg)



## sipu/birch1 (n=100000, d=2) <a name="birch1"></a>

#### sklearn_kmeans (NCA=0.96)

![](sipu/birch1.result100.sklearn_kmeans.jpg)



#### GIc (NCA=0.95)

![](sipu/birch1.result100.GIc.jpg)



#### Genie_G0.1 (NCA=0.94)

![](sipu/birch1.result100.Genie_G0.1.jpg)



#### Genie_G0.3 (NCA=0.94)

![](sipu/birch1.result100.Genie_G0.3.jpg)



#### fastcluster_centroid (NCA=0.92)

![](sipu/birch1.result100.fastcluster_centroid.jpg)



#### fastcluster_ward (NCA=0.91)

![](sipu/birch1.result100.fastcluster_ward.jpg)



#### Genie_G0.5 (NCA=0.80)

![](sipu/birch1.result100.Genie_G0.5.jpg)



#### ITM (NCA=0.80)

![](sipu/birch1.result100.ITM.jpg)



#### IcA (NCA=0.79)

![](sipu/birch1.result100.IcA.jpg)



#### fastcluster_median (NCA=0.60)

![](sipu/birch1.result100.fastcluster_median.jpg)



#### Genie_G0.7 (NCA=0.45)

![](sipu/birch1.result100.Genie_G0.7.jpg)



#### Genie_G1.0 (NCA=0.00)

![](sipu/birch1.result100.Genie_G1.0.jpg)



## sipu/birch2 (n=100000, d=2) <a name="birch2"></a>

#### Genie_G0.1 (NCA=1.00)

![](sipu/birch2.result100.Genie_G0.1.jpg)



#### Genie_G0.3 (NCA=1.00)

![](sipu/birch2.result100.Genie_G0.3.jpg)



#### Genie_G0.5 (NCA=1.00)

![](sipu/birch2.result100.Genie_G0.5.jpg)



#### Genie_G0.7 (NCA=1.00)

![](sipu/birch2.result100.Genie_G0.7.jpg)



#### GIc (NCA=1.00)

![](sipu/birch2.result100.GIc.jpg)



#### fastcluster_ward (NCA=1.00)

![](sipu/birch2.result100.fastcluster_ward.jpg)



#### fastcluster_centroid (NCA=1.00)

![](sipu/birch2.result100.fastcluster_centroid.jpg)



#### sklearn_kmeans (NCA=0.99)

![](sipu/birch2.result100.sklearn_kmeans.jpg)



#### fastcluster_median (NCA=0.98)

![](sipu/birch2.result100.fastcluster_median.jpg)



#### ITM (NCA=0.77)

![](sipu/birch2.result100.ITM.jpg)



#### IcA (NCA=0.77)

![](sipu/birch2.result100.IcA.jpg)



#### Genie_G1.0 (NCA=0.59)

![](sipu/birch2.result100.Genie_G1.0.jpg)



## sipu/compound (n=399, d=2) <a name="compound"></a>

#### fastcluster_ward (NCA=0.87)

![](sipu/compound.result4.fastcluster_ward.jpg)
![](sipu/compound.result5.fastcluster_ward.jpg)
![](sipu/compound.result6.fastcluster_ward.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.87)

![](sipu/compound.result4.sklearn_birch_T0.01_BF50.jpg)
![](sipu/compound.result5.sklearn_birch_T0.01_BF50.jpg)
![](sipu/compound.result6.sklearn_birch_T0.01_BF50.jpg)



#### FCPS_MinEnergy (NCA=0.87)

![](sipu/compound.result4.FCPS_MinEnergy.jpg)
![](sipu/compound.result5.FCPS_MinEnergy.jpg)
![](sipu/compound.result6.FCPS_MinEnergy.jpg)



#### Genie_G0.3 (NCA=0.87)

![](sipu/compound.result4.Genie_G0.3.jpg)
![](sipu/compound.result5.Genie_G0.3.jpg)
![](sipu/compound.result6.Genie_G0.3.jpg)



#### Genie_G0.1 (NCA=0.84)

![](sipu/compound.result4.Genie_G0.1.jpg)
![](sipu/compound.result5.Genie_G0.1.jpg)
![](sipu/compound.result6.Genie_G0.1.jpg)



#### GIc (NCA=0.84)

![](sipu/compound.result4.GIc.jpg)
![](sipu/compound.result5.GIc.jpg)
![](sipu/compound.result6.GIc.jpg)



#### sklearn_gm (NCA=0.84)

![](sipu/compound.result4.sklearn_gm.jpg)
![](sipu/compound.result5.sklearn_gm.jpg)
![](sipu/compound.result6.sklearn_gm.jpg)



#### IcA (NCA=0.84)

![](sipu/compound.result4.IcA.jpg)
![](sipu/compound.result5.IcA.jpg)
![](sipu/compound.result6.IcA.jpg)



#### WCNN_25 (NCA=0.82)

![](sipu/compound.result4.WCNN_25.jpg)
![](sipu/compound.result5.WCNN_25.jpg)
![](sipu/compound.result6.WCNN_25.jpg)



#### CalinskiHarabasz (NCA=0.82)

![](sipu/compound.result4.CalinskiHarabasz.jpg)
![](sipu/compound.result5.CalinskiHarabasz.jpg)
![](sipu/compound.result6.CalinskiHarabasz.jpg)



#### sklearn_kmeans (NCA=0.81)

![](sipu/compound.result4.sklearn_kmeans.jpg)
![](sipu/compound.result5.sklearn_kmeans.jpg)
![](sipu/compound.result6.sklearn_kmeans.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.79)

![](sipu/compound.result4.mst_divisive_DuNN_25_Min_Max.jpg)
![](sipu/compound.result5.mst_divisive_DuNN_25_Min_Max.jpg)
![](sipu/compound.result6.mst_divisive_DuNN_25_Min_Max.jpg)



#### ITM (NCA=0.79)

![](sipu/compound.result4.ITM.jpg)
![](sipu/compound.result5.ITM.jpg)
![](sipu/compound.result6.ITM.jpg)



#### BallHall (NCA=0.79)

![](sipu/compound.result4.BallHall.jpg)
![](sipu/compound.result5.BallHall.jpg)
![](sipu/compound.result6.BallHall.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.78)

![](sipu/compound.result4.sklearn_spectral_Alaplacian_G5.jpg)
![](sipu/compound.result5.sklearn_spectral_Alaplacian_G5.jpg)
![](sipu/compound.result6.sklearn_spectral_Alaplacian_G5.jpg)



#### DuNN_25_Min_Max (NCA=0.78)

![](sipu/compound.result4.DuNN_25_Min_Max.jpg)
![](sipu/compound.result5.DuNN_25_Min_Max.jpg)
![](sipu/compound.result6.DuNN_25_Min_Max.jpg)



#### GDunn_d2_D3 (NCA=0.78)

![](sipu/compound.result4.GDunn_d2_D3.jpg)
![](sipu/compound.result5.GDunn_d2_D3.jpg)
![](sipu/compound.result6.GDunn_d2_D3.jpg)



#### FCPS_Clara (NCA=0.77)

![](sipu/compound.result4.FCPS_Clara.jpg)
![](sipu/compound.result5.FCPS_Clara.jpg)
![](sipu/compound.result6.FCPS_Clara.jpg)



#### FCPS_PAM (NCA=0.76)

![](sipu/compound.result4.FCPS_PAM.jpg)
![](sipu/compound.result5.FCPS_PAM.jpg)
![](sipu/compound.result6.FCPS_PAM.jpg)



#### Genie_G0.5 (NCA=0.76)

![](sipu/compound.result4.Genie_G0.5.jpg)
![](sipu/compound.result5.Genie_G0.5.jpg)
![](sipu/compound.result6.Genie_G0.5.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.75)

![](sipu/compound.result4.FCPS_AdaptiveDensityPeak.jpg)
![](sipu/compound.result5.FCPS_AdaptiveDensityPeak.jpg)
![](sipu/compound.result6.FCPS_AdaptiveDensityPeak.jpg)



#### DuNN_25_Mean_Mean (NCA=0.75)

![](sipu/compound.result4.DuNN_25_Mean_Mean.jpg)
![](sipu/compound.result5.DuNN_25_Mean_Mean.jpg)
![](sipu/compound.result6.DuNN_25_Mean_Mean.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.75)

![](sipu/compound.result4.mst_divisive_CalinskiHarabasz.jpg)
![](sipu/compound.result5.mst_divisive_CalinskiHarabasz.jpg)
![](sipu/compound.result6.mst_divisive_CalinskiHarabasz.jpg)



#### GDunn_d2_D2 (NCA=0.74)

![](sipu/compound.result4.GDunn_d2_D2.jpg)
![](sipu/compound.result5.GDunn_d2_D2.jpg)
![](sipu/compound.result6.GDunn_d2_D2.jpg)



#### fastcluster_median (NCA=0.74)

![](sipu/compound.result4.fastcluster_median.jpg)
![](sipu/compound.result5.fastcluster_median.jpg)
![](sipu/compound.result6.fastcluster_median.jpg)



#### fastcluster_centroid (NCA=0.73)

![](sipu/compound.result4.fastcluster_centroid.jpg)
![](sipu/compound.result5.fastcluster_centroid.jpg)
![](sipu/compound.result6.fastcluster_centroid.jpg)



#### HEMST (NCA=0.73)

![](sipu/compound.result4.HEMST.jpg)
![](sipu/compound.result5.HEMST.jpg)
![](sipu/compound.result6.HEMST.jpg)



#### GDunn_d4_D3 (NCA=0.72)

![](sipu/compound.result4.GDunn_d4_D3.jpg)
![](sipu/compound.result5.GDunn_d4_D3.jpg)
![](sipu/compound.result6.GDunn_d4_D3.jpg)



#### GDunn_d3_D2 (NCA=0.72)

![](sipu/compound.result4.GDunn_d3_D2.jpg)
![](sipu/compound.result5.GDunn_d3_D2.jpg)
![](sipu/compound.result6.GDunn_d3_D2.jpg)



#### FCPS_Fanny (NCA=0.72)

![](sipu/compound.result4.FCPS_Fanny.jpg)
![](sipu/compound.result5.FCPS_Fanny.jpg)
![](sipu/compound.result6.FCPS_Fanny.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.71)

![](sipu/compound.result4.mst_divisive_DuNN_25_Mean_Mean.jpg)
![](sipu/compound.result5.mst_divisive_DuNN_25_Mean_Mean.jpg)
![](sipu/compound.result6.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### GDunn_d3_D3 (NCA=0.71)

![](sipu/compound.result4.GDunn_d3_D3.jpg)
![](sipu/compound.result5.GDunn_d3_D3.jpg)
![](sipu/compound.result6.GDunn_d3_D3.jpg)



#### CTCEHC (NCA=0.70)

![](sipu/compound.result4.CTCEHC.jpg)
![](sipu/compound.result5.CTCEHC.jpg)
![](sipu/compound.result6.CTCEHC.jpg)



#### mst_divisive_Silhouette (NCA=0.69)

![](sipu/compound.result4.mst_divisive_Silhouette.jpg)
![](sipu/compound.result5.mst_divisive_Silhouette.jpg)
![](sipu/compound.result6.mst_divisive_Silhouette.jpg)



#### GDunn_d4_D2 (NCA=0.69)

![](sipu/compound.result4.GDunn_d4_D2.jpg)
![](sipu/compound.result5.GDunn_d4_D2.jpg)
![](sipu/compound.result6.GDunn_d4_D2.jpg)



#### FCPS_Softcl (NCA=0.68)

![](sipu/compound.result4.FCPS_Softcl.jpg)
![](sipu/compound.result5.FCPS_Softcl.jpg)
![](sipu/compound.result6.FCPS_Softcl.jpg)



#### mst_divisive_BallHall (NCA=0.68)

![](sipu/compound.result4.mst_divisive_BallHall.jpg)
![](sipu/compound.result5.mst_divisive_BallHall.jpg)
![](sipu/compound.result6.mst_divisive_BallHall.jpg)



#### mst_divisive_WCNN_25 (NCA=0.67)

![](sipu/compound.result4.mst_divisive_WCNN_25.jpg)
![](sipu/compound.result5.mst_divisive_WCNN_25.jpg)
![](sipu/compound.result6.mst_divisive_WCNN_25.jpg)



#### FCPS_Hardcl (NCA=0.67)

![](sipu/compound.result4.FCPS_Hardcl.jpg)
![](sipu/compound.result5.FCPS_Hardcl.jpg)
![](sipu/compound.result6.FCPS_Hardcl.jpg)



#### Genie_G1.0 (NCA=0.67)

![](sipu/compound.result4.Genie_G1.0.jpg)
![](sipu/compound.result5.Genie_G1.0.jpg)
![](sipu/compound.result6.Genie_G1.0.jpg)



#### GDunn_d1_D3 (NCA=0.67)

![](sipu/compound.result4.GDunn_d1_D3.jpg)
![](sipu/compound.result5.GDunn_d1_D3.jpg)
![](sipu/compound.result6.GDunn_d1_D3.jpg)



#### GDunn_d1_D2 (NCA=0.67)

![](sipu/compound.result4.GDunn_d1_D2.jpg)
![](sipu/compound.result5.GDunn_d1_D2.jpg)
![](sipu/compound.result6.GDunn_d1_D2.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.67)

![](sipu/compound.result4.FCPS_HDBSCAN_2.jpg)
![](sipu/compound.result5.FCPS_HDBSCAN_2.jpg)
![](sipu/compound.result6.FCPS_HDBSCAN_2.jpg)



#### GDunn_d1_D1 (NCA=0.67)

![](sipu/compound.result4.GDunn_d1_D1.jpg)
![](sipu/compound.result5.GDunn_d1_D1.jpg)
![](sipu/compound.result6.GDunn_d1_D1.jpg)



#### Genie_G0.7 (NCA=0.67)

![](sipu/compound.result4.Genie_G0.7.jpg)
![](sipu/compound.result5.Genie_G0.7.jpg)
![](sipu/compound.result6.Genie_G0.7.jpg)



#### fastcluster_weighted (NCA=0.67)

![](sipu/compound.result4.fastcluster_weighted.jpg)
![](sipu/compound.result5.fastcluster_weighted.jpg)
![](sipu/compound.result6.fastcluster_weighted.jpg)



#### fastcluster_complete (NCA=0.67)

![](sipu/compound.result4.fastcluster_complete.jpg)
![](sipu/compound.result5.fastcluster_complete.jpg)
![](sipu/compound.result6.fastcluster_complete.jpg)



#### fastcluster_average (NCA=0.67)

![](sipu/compound.result4.fastcluster_average.jpg)
![](sipu/compound.result5.fastcluster_average.jpg)
![](sipu/compound.result6.fastcluster_average.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.67)

![](sipu/compound.result4.mst_divisive_GDunn_d1_D1.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d1_D1.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.67)

![](sipu/compound.result4.mst_divisive_GDunn_d1_D2.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d1_D2.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.67)

![](sipu/compound.result4.mst_divisive_GDunn_d1_D3.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d1_D3.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d1_D3.jpg)



#### Silhouette (NCA=0.66)

![](sipu/compound.result4.Silhouette.jpg)
![](sipu/compound.result5.Silhouette.jpg)
![](sipu/compound.result6.Silhouette.jpg)



#### GDunn_d5_D2 (NCA=0.65)

![](sipu/compound.result4.GDunn_d5_D2.jpg)
![](sipu/compound.result5.GDunn_d5_D2.jpg)
![](sipu/compound.result6.GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.63)

![](sipu/compound.result4.mst_divisive_GDunn_d3_D3.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d3_D3.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d3_D3.jpg)



#### GDunn_d4_D1 (NCA=0.62)

![](sipu/compound.result4.GDunn_d4_D1.jpg)
![](sipu/compound.result5.GDunn_d4_D1.jpg)
![](sipu/compound.result6.GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.61)

![](sipu/compound.result4.mst_divisive_GDunn_d4_D3.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d4_D3.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.61)

![](sipu/compound.result4.mst_divisive_GDunn_d4_D2.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d4_D2.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.61)

![](sipu/compound.result4.mst_divisive_GDunn_d5_D3.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d5_D3.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d5_D3.jpg)



#### FCPS_Minimax (NCA=0.61)

![](sipu/compound.result4.FCPS_Minimax.jpg)
![](sipu/compound.result5.FCPS_Minimax.jpg)
![](sipu/compound.result6.FCPS_Minimax.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.61)

![](sipu/compound.result4.mst_divisive_GDunn_d5_D2.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d5_D2.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d5_D2.jpg)



#### GDunn_d3_D1 (NCA=0.60)

![](sipu/compound.result4.GDunn_d3_D1.jpg)
![](sipu/compound.result5.GDunn_d3_D1.jpg)
![](sipu/compound.result6.GDunn_d3_D1.jpg)



#### GDunn_d2_D1 (NCA=0.58)

![](sipu/compound.result4.GDunn_d2_D1.jpg)
![](sipu/compound.result5.GDunn_d2_D1.jpg)
![](sipu/compound.result6.GDunn_d2_D1.jpg)



#### DaviesBouldin (NCA=0.58)

![](sipu/compound.result4.DaviesBouldin.jpg)
![](sipu/compound.result5.DaviesBouldin.jpg)
![](sipu/compound.result6.DaviesBouldin.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.57)

![](sipu/compound.result4.mst_divisive_GDunn_d5_D1.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d5_D1.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.57)

![](sipu/compound.result4.mst_divisive_GDunn_d2_D1.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d2_D1.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.55)

![](sipu/compound.result4.mst_divisive_GDunn_d3_D2.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d3_D2.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.55)

![](sipu/compound.result4.mst_divisive_GDunn_d2_D2.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d2_D2.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.55)

![](sipu/compound.result4.mst_divisive_GDunn_d2_D3.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d2_D3.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d2_D3.jpg)



#### FCPS_Diana (NCA=0.55)

![](sipu/compound.result4.FCPS_Diana.jpg)
![](sipu/compound.result5.FCPS_Diana.jpg)
![](sipu/compound.result6.FCPS_Diana.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.51)

![](sipu/compound.result4.mst_divisive_DuNN_25_Max_Min.jpg)
![](sipu/compound.result5.mst_divisive_DuNN_25_Max_Min.jpg)
![](sipu/compound.result6.mst_divisive_DuNN_25_Max_Min.jpg)



#### DuNN_25_Max_Min (NCA=0.45)

![](sipu/compound.result4.DuNN_25_Max_Min.jpg)
![](sipu/compound.result5.DuNN_25_Max_Min.jpg)
![](sipu/compound.result6.DuNN_25_Max_Min.jpg)



#### SilhouetteW (NCA=0.34)

![](sipu/compound.result4.SilhouetteW.jpg)
![](sipu/compound.result5.SilhouetteW.jpg)
![](sipu/compound.result6.SilhouetteW.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.34)

![](sipu/compound.result4.mst_divisive_GDunn_d4_D1.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d4_D1.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.34)

![](sipu/compound.result4.mst_divisive_GDunn_d3_D1.jpg)
![](sipu/compound.result5.mst_divisive_GDunn_d3_D1.jpg)
![](sipu/compound.result6.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_SilhouetteW (NCA=0.33)

![](sipu/compound.result4.mst_divisive_SilhouetteW.jpg)
![](sipu/compound.result5.mst_divisive_SilhouetteW.jpg)
![](sipu/compound.result6.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.33)

![](sipu/compound.result4.mst_divisive_DaviesBouldin.jpg)
![](sipu/compound.result5.mst_divisive_DaviesBouldin.jpg)
![](sipu/compound.result6.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.33)

![](sipu/compound.result4.FCPS_HDBSCAN_4.jpg)
![](sipu/compound.result5.FCPS_HDBSCAN_4.jpg)
![](sipu/compound.result6.FCPS_HDBSCAN_4.jpg)



#### GDunn_d5_D1 (NCA=0.28)

![](sipu/compound.result4.GDunn_d5_D1.jpg)
![](sipu/compound.result5.GDunn_d5_D1.jpg)
![](sipu/compound.result6.GDunn_d5_D1.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.25)

![](sipu/compound.result4.FCPS_HDBSCAN_8.jpg)
![](sipu/compound.result5.FCPS_HDBSCAN_8.jpg)
![](sipu/compound.result6.FCPS_HDBSCAN_8.jpg)



#### GDunn_d5_D3 (NCA=0.11)

![](sipu/compound.result4.GDunn_d5_D3.jpg)
![](sipu/compound.result5.GDunn_d5_D3.jpg)
![](sipu/compound.result6.GDunn_d5_D3.jpg)



## sipu/d31 (n=3100, d=2) <a name="d31"></a>

#### sklearn_kmeans (NCA=0.98)

![](sipu/d31.result31.sklearn_kmeans.jpg)



#### FCPS_PAM (NCA=0.98)

![](sipu/d31.result31.FCPS_PAM.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.98)

![](sipu/d31.result31.FCPS_AdaptiveDensityPeak.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.97)

![](sipu/d31.result31.sklearn_spectral_Alaplacian_G5.jpg)



#### sklearn_gm (NCA=0.97)

![](sipu/d31.result31.sklearn_gm.jpg)



#### mst_divisive_WCNN_25 (NCA=0.97)

![](sipu/d31.result31.mst_divisive_WCNN_25.jpg)



#### Genie_G0.1 (NCA=0.97)

![](sipu/d31.result31.Genie_G0.1.jpg)



#### CTCEHC (NCA=0.96)

![](sipu/d31.result31.CTCEHC.jpg)



#### GIc (NCA=0.96)

![](sipu/d31.result31.GIc.jpg)



#### fastcluster_complete (NCA=0.96)

![](sipu/d31.result31.fastcluster_complete.jpg)



#### fastcluster_ward (NCA=0.96)

![](sipu/d31.result31.fastcluster_ward.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.96)

![](sipu/d31.result31.sklearn_birch_T0.01_BF50.jpg)



#### FCPS_MinEnergy (NCA=0.96)

![](sipu/d31.result31.FCPS_MinEnergy.jpg)



#### FCPS_Clara (NCA=0.94)

![](sipu/d31.result31.FCPS_Clara.jpg)



#### fastcluster_centroid (NCA=0.94)

![](sipu/d31.result31.fastcluster_centroid.jpg)



#### fastcluster_average (NCA=0.94)

![](sipu/d31.result31.fastcluster_average.jpg)



#### FCPS_Minimax (NCA=0.93)

![](sipu/d31.result31.FCPS_Minimax.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.93)

![](sipu/d31.result31.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.93)

![](sipu/d31.result31.mst_divisive_CalinskiHarabasz.jpg)



#### FCPS_Softcl (NCA=0.93)

![](sipu/d31.result31.FCPS_Softcl.jpg)



#### Genie_G0.3 (NCA=0.93)

![](sipu/d31.result31.Genie_G0.3.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.92)

![](sipu/d31.result31.mst_divisive_DuNN_25_Min_Max.jpg)



#### FCPS_Hardcl (NCA=0.88)

![](sipu/d31.result31.FCPS_Hardcl.jpg)



#### mst_divisive_Silhouette (NCA=0.86)

![](sipu/d31.result31.mst_divisive_Silhouette.jpg)



#### FCPS_Diana (NCA=0.85)

![](sipu/d31.result31.FCPS_Diana.jpg)



#### ITM (NCA=0.85)

![](sipu/d31.result31.ITM.jpg)



#### fastcluster_median (NCA=0.83)

![](sipu/d31.result31.fastcluster_median.jpg)



#### fastcluster_weighted (NCA=0.82)

![](sipu/d31.result31.fastcluster_weighted.jpg)



#### IcA (NCA=0.80)

![](sipu/d31.result31.IcA.jpg)



#### Genie_G0.5 (NCA=0.76)

![](sipu/d31.result31.Genie_G0.5.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.74)

![](sipu/d31.result31.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.73)

![](sipu/d31.result31.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_BallHall (NCA=0.72)

![](sipu/d31.result31.mst_divisive_BallHall.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.70)

![](sipu/d31.result31.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.67)

![](sipu/d31.result31.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.66)

![](sipu/d31.result31.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.66)

![](sipu/d31.result31.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.58)

![](sipu/d31.result31.mst_divisive_DuNN_25_Max_Min.jpg)



#### HEMST (NCA=0.55)

![](sipu/d31.result31.HEMST.jpg)



#### Genie_G0.7 (NCA=0.53)

![](sipu/d31.result31.Genie_G0.7.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.27)

![](sipu/d31.result31.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.26)

![](sipu/d31.result31.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.25)

![](sipu/d31.result31.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.25)

![](sipu/d31.result31.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.24)

![](sipu/d31.result31.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.24)

![](sipu/d31.result31.mst_divisive_GDunn_d1_D2.jpg)



#### Genie_G1.0 (NCA=0.24)

![](sipu/d31.result31.Genie_G1.0.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.24)

![](sipu/d31.result31.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.14)

![](sipu/d31.result31.mst_divisive_GDunn_d4_D3.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.14)

![](sipu/d31.result31.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.12)

![](sipu/d31.result31.mst_divisive_GDunn_d4_D2.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.11)

![](sipu/d31.result31.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.09)

![](sipu/d31.result31.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_SilhouetteW (NCA=0.01)

![](sipu/d31.result31.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.01)

![](sipu/d31.result31.mst_divisive_DaviesBouldin.jpg)



## sipu/flame (n=240, d=2) <a name="flame"></a>

#### Genie_G0.1 (NCA=1.00)

![](sipu/flame.result2.Genie_G0.1.jpg)



#### Genie_G0.3 (NCA=1.00)

![](sipu/flame.result2.Genie_G0.3.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/flame.result2.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### CTCEHC (NCA=1.00)

![](sipu/flame.result2.CTCEHC.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=1.00)

![](sipu/flame.result2.mst_divisive_DuNN_25_Min_Max.jpg)



#### DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/flame.result2.DuNN_25_Mean_Mean.jpg)



#### Genie_G0.5 (NCA=1.00)

![](sipu/flame.result2.Genie_G0.5.jpg)



#### Genie_G0.7 (NCA=1.00)

![](sipu/flame.result2.Genie_G0.7.jpg)



#### GIc (NCA=1.00)

![](sipu/flame.result2.GIc.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.93)

![](sipu/flame.result2.sklearn_spectral_Alaplacian_G5.jpg)



#### FCPS_Minimax (NCA=0.90)

![](sipu/flame.result2.FCPS_Minimax.jpg)



#### FCPS_Diana (NCA=0.79)

![](sipu/flame.result2.FCPS_Diana.jpg)



#### Silhouette (NCA=0.79)

![](sipu/flame.result2.Silhouette.jpg)



#### GDunn_d2_D3 (NCA=0.78)

![](sipu/flame.result2.GDunn_d2_D3.jpg)



#### GDunn_d2_D2 (NCA=0.77)

![](sipu/flame.result2.GDunn_d2_D2.jpg)



#### GDunn_d3_D2 (NCA=0.77)

![](sipu/flame.result2.GDunn_d3_D2.jpg)



#### FCPS_Softcl (NCA=0.77)

![](sipu/flame.result2.FCPS_Softcl.jpg)



#### FCPS_Clara (NCA=0.77)

![](sipu/flame.result2.FCPS_Clara.jpg)



#### GDunn_d3_D3 (NCA=0.77)

![](sipu/flame.result2.GDunn_d3_D3.jpg)



#### DuNN_25_Max_Min (NCA=0.76)

![](sipu/flame.result2.DuNN_25_Max_Min.jpg)



#### GDunn_d5_D3 (NCA=0.76)

![](sipu/flame.result2.GDunn_d5_D3.jpg)



#### FCPS_PAM (NCA=0.76)

![](sipu/flame.result2.FCPS_PAM.jpg)



#### FCPS_Hardcl (NCA=0.75)

![](sipu/flame.result2.FCPS_Hardcl.jpg)



#### DuNN_25_Min_Max (NCA=0.75)

![](sipu/flame.result2.DuNN_25_Min_Max.jpg)



#### FCPS_Fanny (NCA=0.75)

![](sipu/flame.result2.FCPS_Fanny.jpg)



#### fastcluster_average (NCA=0.74)

![](sipu/flame.result2.fastcluster_average.jpg)



#### CalinskiHarabasz (NCA=0.74)

![](sipu/flame.result2.CalinskiHarabasz.jpg)



#### sklearn_kmeans (NCA=0.74)

![](sipu/flame.result2.sklearn_kmeans.jpg)



#### fastcluster_weighted (NCA=0.73)

![](sipu/flame.result2.fastcluster_weighted.jpg)



#### FCPS_MinEnergy (NCA=0.72)

![](sipu/flame.result2.FCPS_MinEnergy.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.70)

![](sipu/flame.result2.FCPS_AdaptiveDensityPeak.jpg)



#### IcA (NCA=0.68)

![](sipu/flame.result2.IcA.jpg)



#### ITM (NCA=0.68)

![](sipu/flame.result2.ITM.jpg)



#### mst_divisive_Silhouette (NCA=0.68)

![](sipu/flame.result2.mst_divisive_Silhouette.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.68)

![](sipu/flame.result2.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.68)

![](sipu/flame.result2.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.68)

![](sipu/flame.result2.mst_divisive_GDunn_d2_D2.jpg)



#### sklearn_gm (NCA=0.68)

![](sipu/flame.result2.sklearn_gm.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.67)

![](sipu/flame.result2.mst_divisive_GDunn_d2_D1.jpg)



#### fastcluster_median (NCA=0.61)

![](sipu/flame.result2.fastcluster_median.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.59)

![](sipu/flame.result2.sklearn_birch_T0.01_BF50.jpg)



#### fastcluster_ward (NCA=0.59)

![](sipu/flame.result2.fastcluster_ward.jpg)



#### GDunn_d5_D2 (NCA=0.35)

![](sipu/flame.result2.GDunn_d5_D2.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.29)

![](sipu/flame.result2.mst_divisive_DuNN_25_Max_Min.jpg)



#### fastcluster_complete (NCA=0.21)

![](sipu/flame.result2.fastcluster_complete.jpg)



#### GDunn_d2_D1 (NCA=0.20)

![](sipu/flame.result2.GDunn_d2_D1.jpg)



#### WCNN_25 (NCA=0.19)

![](sipu/flame.result2.WCNN_25.jpg)



#### mst_divisive_WCNN_25 (NCA=0.19)

![](sipu/flame.result2.mst_divisive_WCNN_25.jpg)



#### mst_divisive_BallHall (NCA=0.12)

![](sipu/flame.result2.mst_divisive_BallHall.jpg)



#### BallHall (NCA=0.09)

![](sipu/flame.result2.BallHall.jpg)



#### GDunn_d5_D1 (NCA=0.03)

![](sipu/flame.result2.GDunn_d5_D1.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.02)

![](sipu/flame.result2.FCPS_HDBSCAN_2.jpg)



#### fastcluster_centroid (NCA=0.02)

![](sipu/flame.result2.fastcluster_centroid.jpg)



#### Genie_G1.0 (NCA=0.02)

![](sipu/flame.result2.Genie_G1.0.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.02)

![](sipu/flame.result2.mst_divisive_GDunn_d1_D3.jpg)



#### GDunn_d3_D1 (NCA=0.02)

![](sipu/flame.result2.GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.02)

![](sipu/flame.result2.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.02)

![](sipu/flame.result2.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_SilhouetteW (NCA=0.02)

![](sipu/flame.result2.mst_divisive_SilhouetteW.jpg)



#### GDunn_d1_D1 (NCA=0.02)

![](sipu/flame.result2.GDunn_d1_D1.jpg)



#### GDunn_d1_D2 (NCA=0.02)

![](sipu/flame.result2.GDunn_d1_D2.jpg)



#### GDunn_d1_D3 (NCA=0.02)

![](sipu/flame.result2.GDunn_d1_D3.jpg)



#### SilhouetteW (NCA=0.02)

![](sipu/flame.result2.SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.02)

![](sipu/flame.result2.mst_divisive_DaviesBouldin.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.02)

![](sipu/flame.result2.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.02)

![](sipu/flame.result2.mst_divisive_GDunn_d1_D2.jpg)



#### DaviesBouldin (NCA=0.02)

![](sipu/flame.result2.DaviesBouldin.jpg)



#### HEMST (NCA=0.01)

![](sipu/flame.result2.HEMST.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d4_D2.jpg)



#### GDunn_d4_D1 (NCA=0.01)

![](sipu/flame.result2.GDunn_d4_D1.jpg)



#### GDunn_d4_D2 (NCA=0.01)

![](sipu/flame.result2.GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d4_D1.jpg)



#### GDunn_d4_D3 (NCA=0.01)

![](sipu/flame.result2.GDunn_d4_D3.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.01)

![](sipu/flame.result2.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.01)

![](sipu/flame.result2.mst_divisive_GDunn_d3_D3.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.01)

![](sipu/flame.result2.FCPS_HDBSCAN_4.jpg)



## sipu/jain (n=373, d=2) <a name="jain"></a>

#### mst_divisive_GDunn_d1_D1 (NCA=1.00)

![](sipu/jain.result2.mst_divisive_GDunn_d1_D1.jpg)



#### Genie_G0.3 (NCA=1.00)

![](sipu/jain.result2.Genie_G0.3.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=1.00)

![](sipu/jain.result2.mst_divisive_GDunn_d1_D3.jpg)



#### WCNN_25 (NCA=1.00)

![](sipu/jain.result2.WCNN_25.jpg)



#### GDunn_d1_D2 (NCA=1.00)

![](sipu/jain.result2.GDunn_d1_D2.jpg)



#### GDunn_d1_D1 (NCA=1.00)

![](sipu/jain.result2.GDunn_d1_D1.jpg)



#### mst_divisive_WCNN_25 (NCA=1.00)

![](sipu/jain.result2.mst_divisive_WCNN_25.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=1.00)

![](sipu/jain.result2.mst_divisive_GDunn_d1_D2.jpg)



#### GIc (NCA=1.00)

![](sipu/jain.result2.GIc.jpg)



#### Genie_G0.5 (NCA=1.00)

![](sipu/jain.result2.Genie_G0.5.jpg)



#### IcA (NCA=0.99)

![](sipu/jain.result2.IcA.jpg)



#### GDunn_d1_D3 (NCA=0.99)

![](sipu/jain.result2.GDunn_d1_D3.jpg)



#### DuNN_25_Min_Max (NCA=0.97)

![](sipu/jain.result2.DuNN_25_Min_Max.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.94)

![](sipu/jain.result2.mst_divisive_GDunn_d2_D1.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.81)

![](sipu/jain.result2.sklearn_birch_T0.01_BF50.jpg)



#### fastcluster_ward (NCA=0.81)

![](sipu/jain.result2.fastcluster_ward.jpg)



#### FCPS_MinEnergy (NCA=0.81)

![](sipu/jain.result2.FCPS_MinEnergy.jpg)



#### fastcluster_weighted (NCA=0.81)

![](sipu/jain.result2.fastcluster_weighted.jpg)



#### fastcluster_centroid (NCA=0.81)

![](sipu/jain.result2.fastcluster_centroid.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.80)

![](sipu/jain.result2.FCPS_AdaptiveDensityPeak.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.80)

![](sipu/jain.result2.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.80)

![](sipu/jain.result2.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.80)

![](sipu/jain.result2.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.80)

![](sipu/jain.result2.mst_divisive_GDunn_d5_D2.jpg)



#### fastcluster_average (NCA=0.79)

![](sipu/jain.result2.fastcluster_average.jpg)



#### fastcluster_complete (NCA=0.79)

![](sipu/jain.result2.fastcluster_complete.jpg)



#### GDunn_d2_D2 (NCA=0.76)

![](sipu/jain.result2.GDunn_d2_D2.jpg)



#### GDunn_d4_D2 (NCA=0.75)

![](sipu/jain.result2.GDunn_d4_D2.jpg)



#### GDunn_d3_D2 (NCA=0.75)

![](sipu/jain.result2.GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.75)

![](sipu/jain.result2.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.75)

![](sipu/jain.result2.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.75)

![](sipu/jain.result2.mst_divisive_GDunn_d4_D3.jpg)



#### GDunn_d3_D3 (NCA=0.74)

![](sipu/jain.result2.GDunn_d3_D3.jpg)



#### GDunn_d2_D3 (NCA=0.74)

![](sipu/jain.result2.GDunn_d2_D3.jpg)



#### FCPS_Minimax (NCA=0.73)

![](sipu/jain.result2.FCPS_Minimax.jpg)



#### GDunn_d4_D3 (NCA=0.73)

![](sipu/jain.result2.GDunn_d4_D3.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.72)

![](sipu/jain.result2.sklearn_spectral_Alaplacian_G5.jpg)



#### ITM (NCA=0.71)

![](sipu/jain.result2.ITM.jpg)



#### Silhouette (NCA=0.71)

![](sipu/jain.result2.Silhouette.jpg)



#### FCPS_Diana (NCA=0.71)

![](sipu/jain.result2.FCPS_Diana.jpg)



#### sklearn_kmeans (NCA=0.70)

![](sipu/jain.result2.sklearn_kmeans.jpg)



#### CalinskiHarabasz (NCA=0.70)

![](sipu/jain.result2.CalinskiHarabasz.jpg)



#### FCPS_Softcl (NCA=0.69)

![](sipu/jain.result2.FCPS_Softcl.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.69)

![](sipu/jain.result2.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_Silhouette (NCA=0.69)

![](sipu/jain.result2.mst_divisive_Silhouette.jpg)



#### FCPS_Hardcl (NCA=0.68)

![](sipu/jain.result2.FCPS_Hardcl.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.68)

![](sipu/jain.result2.mst_divisive_DuNN_25_Max_Min.jpg)



#### FCPS_Fanny (NCA=0.66)

![](sipu/jain.result2.FCPS_Fanny.jpg)



#### FCPS_PAM (NCA=0.66)

![](sipu/jain.result2.FCPS_PAM.jpg)



#### fastcluster_median (NCA=0.65)

![](sipu/jain.result2.fastcluster_median.jpg)



#### FCPS_Clara (NCA=0.65)

![](sipu/jain.result2.FCPS_Clara.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.60)

![](sipu/jain.result2.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.60)

![](sipu/jain.result2.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.60)

![](sipu/jain.result2.mst_divisive_GDunn_d5_D1.jpg)



#### GDunn_d3_D1 (NCA=0.56)

![](sipu/jain.result2.GDunn_d3_D1.jpg)



#### GDunn_d4_D1 (NCA=0.56)

![](sipu/jain.result2.GDunn_d4_D1.jpg)



#### CTCEHC (NCA=0.53)

![](sipu/jain.result2.CTCEHC.jpg)



#### GDunn_d2_D1 (NCA=0.52)

![](sipu/jain.result2.GDunn_d2_D1.jpg)



#### mst_divisive_BallHall (NCA=0.50)

![](sipu/jain.result2.mst_divisive_BallHall.jpg)



#### Genie_G0.1 (NCA=0.49)

![](sipu/jain.result2.Genie_G0.1.jpg)



#### HEMST (NCA=0.49)

![](sipu/jain.result2.HEMST.jpg)



#### BallHall (NCA=0.47)

![](sipu/jain.result2.BallHall.jpg)



#### GDunn_d5_D1 (NCA=0.47)

![](sipu/jain.result2.GDunn_d5_D1.jpg)



#### sklearn_gm (NCA=0.43)

![](sipu/jain.result2.sklearn_gm.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.27)

![](sipu/jain.result2.FCPS_HDBSCAN_2.jpg)



#### Genie_G0.7 (NCA=0.27)

![](sipu/jain.result2.Genie_G0.7.jpg)



#### DuNN_25_Mean_Mean (NCA=0.27)

![](sipu/jain.result2.DuNN_25_Mean_Mean.jpg)



#### Genie_G1.0 (NCA=0.27)

![](sipu/jain.result2.Genie_G1.0.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.27)

![](sipu/jain.result2.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.27)

![](sipu/jain.result2.mst_divisive_DuNN_25_Min_Max.jpg)



#### GDunn_d5_D2 (NCA=0.21)

![](sipu/jain.result2.GDunn_d5_D2.jpg)



#### DuNN_25_Max_Min (NCA=0.14)

![](sipu/jain.result2.DuNN_25_Max_Min.jpg)



#### SilhouetteW (NCA=0.02)

![](sipu/jain.result2.SilhouetteW.jpg)



#### DaviesBouldin (NCA=0.02)

![](sipu/jain.result2.DaviesBouldin.jpg)



#### mst_divisive_SilhouetteW (NCA=0.02)

![](sipu/jain.result2.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.02)

![](sipu/jain.result2.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.01)

![](sipu/jain.result2.FCPS_HDBSCAN_8.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.01)

![](sipu/jain.result2.FCPS_HDBSCAN_4.jpg)



#### GDunn_d5_D3 (NCA=0.00)

![](sipu/jain.result2.GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.00)

![](sipu/jain.result2.mst_divisive_GDunn_d5_D3.jpg)



## sipu/pathbased (n=300, d=2) <a name="pathbased"></a>

#### Genie_G0.1 (NCA=0.98)

![](sipu/pathbased.result3.Genie_G0.1.jpg)
![](sipu/pathbased.result4.Genie_G0.1.jpg)



#### Genie_G0.3 (NCA=0.98)

![](sipu/pathbased.result3.Genie_G0.3.jpg)
![](sipu/pathbased.result4.Genie_G0.3.jpg)



#### GIc (NCA=0.98)

![](sipu/pathbased.result3.GIc.jpg)
![](sipu/pathbased.result4.GIc.jpg)



#### IcA (NCA=0.82)

![](sipu/pathbased.result3.IcA.jpg)
![](sipu/pathbased.result4.IcA.jpg)



#### mst_divisive_Silhouette (NCA=0.80)

![](sipu/pathbased.result3.mst_divisive_Silhouette.jpg)
![](sipu/pathbased.result4.mst_divisive_Silhouette.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.76)

![](sipu/pathbased.result3.mst_divisive_DuNN_25_Max_Min.jpg)
![](sipu/pathbased.result4.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.76)

![](sipu/pathbased.result3.mst_divisive_DuNN_25_Min_Max.jpg)
![](sipu/pathbased.result4.mst_divisive_DuNN_25_Min_Max.jpg)



#### Genie_G0.7 (NCA=0.76)

![](sipu/pathbased.result3.Genie_G0.7.jpg)
![](sipu/pathbased.result4.Genie_G0.7.jpg)



#### Genie_G0.5 (NCA=0.76)

![](sipu/pathbased.result3.Genie_G0.5.jpg)
![](sipu/pathbased.result4.Genie_G0.5.jpg)



#### DuNN_25_Min_Max (NCA=0.75)

![](sipu/pathbased.result3.DuNN_25_Min_Max.jpg)
![](sipu/pathbased.result4.DuNN_25_Min_Max.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.72)

![](sipu/pathbased.result3.mst_divisive_CalinskiHarabasz.jpg)
![](sipu/pathbased.result4.mst_divisive_CalinskiHarabasz.jpg)



#### ITM (NCA=0.68)

![](sipu/pathbased.result3.ITM.jpg)
![](sipu/pathbased.result4.ITM.jpg)



#### fastcluster_ward (NCA=0.67)

![](sipu/pathbased.result3.fastcluster_ward.jpg)
![](sipu/pathbased.result4.fastcluster_ward.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.67)

![](sipu/pathbased.result3.sklearn_birch_T0.01_BF50.jpg)
![](sipu/pathbased.result4.sklearn_birch_T0.01_BF50.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.67)

![](sipu/pathbased.result3.FCPS_AdaptiveDensityPeak.jpg)
![](sipu/pathbased.result4.FCPS_AdaptiveDensityPeak.jpg)



#### FCPS_Softcl (NCA=0.65)

![](sipu/pathbased.result3.FCPS_Softcl.jpg)
![](sipu/pathbased.result4.FCPS_Softcl.jpg)



#### CalinskiHarabasz (NCA=0.65)

![](sipu/pathbased.result3.CalinskiHarabasz.jpg)
![](sipu/pathbased.result4.CalinskiHarabasz.jpg)



#### Silhouette (NCA=0.65)

![](sipu/pathbased.result3.Silhouette.jpg)
![](sipu/pathbased.result4.Silhouette.jpg)



#### sklearn_kmeans (NCA=0.65)

![](sipu/pathbased.result3.sklearn_kmeans.jpg)
![](sipu/pathbased.result4.sklearn_kmeans.jpg)



#### FCPS_Hardcl (NCA=0.65)

![](sipu/pathbased.result3.FCPS_Hardcl.jpg)
![](sipu/pathbased.result4.FCPS_Hardcl.jpg)



#### GDunn_d3_D1 (NCA=0.65)

![](sipu/pathbased.result3.GDunn_d3_D1.jpg)
![](sipu/pathbased.result4.GDunn_d3_D1.jpg)



#### GDunn_d4_D1 (NCA=0.65)

![](sipu/pathbased.result3.GDunn_d4_D1.jpg)
![](sipu/pathbased.result4.GDunn_d4_D1.jpg)



#### FCPS_PAM (NCA=0.65)

![](sipu/pathbased.result3.FCPS_PAM.jpg)
![](sipu/pathbased.result4.FCPS_PAM.jpg)



#### fastcluster_median (NCA=0.65)

![](sipu/pathbased.result3.fastcluster_median.jpg)
![](sipu/pathbased.result4.fastcluster_median.jpg)



#### FCPS_Clara (NCA=0.65)

![](sipu/pathbased.result3.FCPS_Clara.jpg)
![](sipu/pathbased.result4.FCPS_Clara.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.65)

![](sipu/pathbased.result3.sklearn_spectral_Alaplacian_G5.jpg)
![](sipu/pathbased.result4.sklearn_spectral_Alaplacian_G5.jpg)



#### DuNN_25_Mean_Mean (NCA=0.64)

![](sipu/pathbased.result3.DuNN_25_Mean_Mean.jpg)
![](sipu/pathbased.result4.DuNN_25_Mean_Mean.jpg)



#### GDunn_d1_D2 (NCA=0.64)

![](sipu/pathbased.result3.GDunn_d1_D2.jpg)
![](sipu/pathbased.result4.GDunn_d1_D2.jpg)



#### fastcluster_centroid (NCA=0.64)

![](sipu/pathbased.result3.fastcluster_centroid.jpg)
![](sipu/pathbased.result4.fastcluster_centroid.jpg)



#### fastcluster_average (NCA=0.63)

![](sipu/pathbased.result3.fastcluster_average.jpg)
![](sipu/pathbased.result4.fastcluster_average.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.62)

![](sipu/pathbased.result3.mst_divisive_GDunn_d5_D1.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d5_D1.jpg)



#### GDunn_d2_D3 (NCA=0.62)

![](sipu/pathbased.result3.GDunn_d2_D3.jpg)
![](sipu/pathbased.result4.GDunn_d2_D3.jpg)



#### GDunn_d3_D2 (NCA=0.62)

![](sipu/pathbased.result3.GDunn_d3_D2.jpg)
![](sipu/pathbased.result4.GDunn_d3_D2.jpg)



#### GDunn_d2_D2 (NCA=0.62)

![](sipu/pathbased.result3.GDunn_d2_D2.jpg)
![](sipu/pathbased.result4.GDunn_d2_D2.jpg)



#### GDunn_d1_D3 (NCA=0.62)

![](sipu/pathbased.result3.GDunn_d1_D3.jpg)
![](sipu/pathbased.result4.GDunn_d1_D3.jpg)



#### WCNN_25 (NCA=0.62)

![](sipu/pathbased.result3.WCNN_25.jpg)
![](sipu/pathbased.result4.WCNN_25.jpg)



#### mst_divisive_WCNN_25 (NCA=0.62)

![](sipu/pathbased.result3.mst_divisive_WCNN_25.jpg)
![](sipu/pathbased.result4.mst_divisive_WCNN_25.jpg)



#### FCPS_Diana (NCA=0.62)

![](sipu/pathbased.result3.FCPS_Diana.jpg)
![](sipu/pathbased.result4.FCPS_Diana.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.62)

![](sipu/pathbased.result3.mst_divisive_GDunn_d5_D2.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.61)

![](sipu/pathbased.result3.mst_divisive_GDunn_d5_D3.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d5_D3.jpg)



#### GDunn_d4_D2 (NCA=0.61)

![](sipu/pathbased.result3.GDunn_d4_D2.jpg)
![](sipu/pathbased.result4.GDunn_d4_D2.jpg)



#### sklearn_gm (NCA=0.61)

![](sipu/pathbased.result3.sklearn_gm.jpg)
![](sipu/pathbased.result4.sklearn_gm.jpg)



#### GDunn_d3_D3 (NCA=0.60)

![](sipu/pathbased.result3.GDunn_d3_D3.jpg)
![](sipu/pathbased.result4.GDunn_d3_D3.jpg)



#### GDunn_d4_D3 (NCA=0.60)

![](sipu/pathbased.result3.GDunn_d4_D3.jpg)
![](sipu/pathbased.result4.GDunn_d4_D3.jpg)



#### FCPS_Minimax (NCA=0.60)

![](sipu/pathbased.result3.FCPS_Minimax.jpg)
![](sipu/pathbased.result4.FCPS_Minimax.jpg)



#### GDunn_d1_D1 (NCA=0.60)

![](sipu/pathbased.result3.GDunn_d1_D1.jpg)
![](sipu/pathbased.result4.GDunn_d1_D1.jpg)



#### FCPS_MinEnergy (NCA=0.59)

![](sipu/pathbased.result3.FCPS_MinEnergy.jpg)
![](sipu/pathbased.result4.FCPS_MinEnergy.jpg)



#### HEMST (NCA=0.56)

![](sipu/pathbased.result3.HEMST.jpg)
![](sipu/pathbased.result4.HEMST.jpg)



#### DaviesBouldin (NCA=0.56)

![](sipu/pathbased.result3.DaviesBouldin.jpg)
![](sipu/pathbased.result4.DaviesBouldin.jpg)



#### fastcluster_complete (NCA=0.56)

![](sipu/pathbased.result3.fastcluster_complete.jpg)
![](sipu/pathbased.result4.fastcluster_complete.jpg)



#### BallHall (NCA=0.55)

![](sipu/pathbased.result3.BallHall.jpg)
![](sipu/pathbased.result4.BallHall.jpg)



#### FCPS_Fanny (NCA=0.53)

![](sipu/pathbased.result3.FCPS_Fanny.jpg)
![](sipu/pathbased.result4.FCPS_Fanny.jpg)



#### GDunn_d2_D1 (NCA=0.52)

![](sipu/pathbased.result3.GDunn_d2_D1.jpg)
![](sipu/pathbased.result4.GDunn_d2_D1.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.51)

![](sipu/pathbased.result3.mst_divisive_DuNN_25_Mean_Mean.jpg)
![](sipu/pathbased.result4.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### fastcluster_weighted (NCA=0.46)

![](sipu/pathbased.result3.fastcluster_weighted.jpg)
![](sipu/pathbased.result4.fastcluster_weighted.jpg)



#### GDunn_d5_D2 (NCA=0.39)

![](sipu/pathbased.result3.GDunn_d5_D2.jpg)
![](sipu/pathbased.result4.GDunn_d5_D2.jpg)



#### SilhouetteW (NCA=0.36)

![](sipu/pathbased.result3.SilhouetteW.jpg)
![](sipu/pathbased.result4.SilhouetteW.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.32)

![](sipu/pathbased.result3.mst_divisive_GDunn_d2_D2.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.32)

![](sipu/pathbased.result3.mst_divisive_GDunn_d2_D1.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.31)

![](sipu/pathbased.result3.mst_divisive_GDunn_d2_D3.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d2_D3.jpg)



#### DuNN_25_Max_Min (NCA=0.30)

![](sipu/pathbased.result3.DuNN_25_Max_Min.jpg)
![](sipu/pathbased.result4.DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.29)

![](sipu/pathbased.result3.mst_divisive_GDunn_d3_D1.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.29)

![](sipu/pathbased.result3.mst_divisive_GDunn_d4_D3.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.29)

![](sipu/pathbased.result3.mst_divisive_GDunn_d4_D2.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d4_D2.jpg)



#### GDunn_d5_D1 (NCA=0.28)

![](sipu/pathbased.result3.GDunn_d5_D1.jpg)
![](sipu/pathbased.result4.GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.27)

![](sipu/pathbased.result3.mst_divisive_GDunn_d3_D3.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.27)

![](sipu/pathbased.result3.mst_divisive_GDunn_d3_D2.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d3_D2.jpg)



#### CTCEHC (NCA=0.24)

![](sipu/pathbased.result3.CTCEHC.jpg)
![](sipu/pathbased.result4.CTCEHC.jpg)



#### mst_divisive_BallHall (NCA=0.08)

![](sipu/pathbased.result3.mst_divisive_BallHall.jpg)
![](sipu/pathbased.result4.mst_divisive_BallHall.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.06)

![](sipu/pathbased.result3.mst_divisive_GDunn_d4_D1.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d4_D1.jpg)



#### GDunn_d5_D3 (NCA=0.06)

![](sipu/pathbased.result3.GDunn_d5_D3.jpg)
![](sipu/pathbased.result4.GDunn_d5_D3.jpg)



#### mst_divisive_SilhouetteW (NCA=0.02)

![](sipu/pathbased.result3.mst_divisive_SilhouetteW.jpg)
![](sipu/pathbased.result4.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.01)

![](sipu/pathbased.result3.mst_divisive_DaviesBouldin.jpg)
![](sipu/pathbased.result4.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.01)

![](sipu/pathbased.result3.FCPS_HDBSCAN_8.jpg)
![](sipu/pathbased.result4.FCPS_HDBSCAN_8.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.01)

![](sipu/pathbased.result3.FCPS_HDBSCAN_4.jpg)
![](sipu/pathbased.result4.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.01)

![](sipu/pathbased.result3.mst_divisive_GDunn_d1_D3.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.01)

![](sipu/pathbased.result3.mst_divisive_GDunn_d1_D2.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d1_D2.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.01)

![](sipu/pathbased.result3.FCPS_HDBSCAN_2.jpg)
![](sipu/pathbased.result4.FCPS_HDBSCAN_2.jpg)



#### Genie_G1.0 (NCA=0.01)

![](sipu/pathbased.result3.Genie_G1.0.jpg)
![](sipu/pathbased.result4.Genie_G1.0.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.01)

![](sipu/pathbased.result3.mst_divisive_GDunn_d1_D1.jpg)
![](sipu/pathbased.result4.mst_divisive_GDunn_d1_D1.jpg)



## sipu/r15 (n=600, d=2) <a name="r15"></a>

#### mst_divisive_BallHall (NCA=1.00)

![](sipu/r15.result8.mst_divisive_BallHall.jpg)
![](sipu/r15.result9.mst_divisive_BallHall.jpg)
![](sipu/r15.result15.mst_divisive_BallHall.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=1.00)

![](sipu/r15.result8.mst_divisive_DuNN_25_Max_Min.jpg)
![](sipu/r15.result9.mst_divisive_DuNN_25_Max_Min.jpg)
![](sipu/r15.result15.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/r15.result8.mst_divisive_DuNN_25_Mean_Mean.jpg)
![](sipu/r15.result9.mst_divisive_DuNN_25_Mean_Mean.jpg)
![](sipu/r15.result15.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=1.00)

![](sipu/r15.result8.mst_divisive_DuNN_25_Min_Max.jpg)
![](sipu/r15.result9.mst_divisive_DuNN_25_Min_Max.jpg)
![](sipu/r15.result15.mst_divisive_DuNN_25_Min_Max.jpg)



#### mst_divisive_WCNN_25 (NCA=1.00)

![](sipu/r15.result8.mst_divisive_WCNN_25.jpg)
![](sipu/r15.result9.mst_divisive_WCNN_25.jpg)
![](sipu/r15.result15.mst_divisive_WCNN_25.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=1.00)

![](sipu/r15.result8.mst_divisive_GDunn_d1_D3.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d1_D3.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=1.00)

![](sipu/r15.result8.mst_divisive_GDunn_d1_D2.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d1_D2.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=1.00)

![](sipu/r15.result8.mst_divisive_GDunn_d1_D1.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d1_D1.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d1_D1.jpg)



#### WCNN_25 (NCA=1.00)

![](sipu/r15.result8.WCNN_25.jpg)
![](sipu/r15.result9.WCNN_25.jpg)
![](sipu/r15.result15.WCNN_25.jpg)



#### SilhouetteW (NCA=1.00)

![](sipu/r15.result8.SilhouetteW.jpg)
![](sipu/r15.result9.SilhouetteW.jpg)
![](sipu/r15.result15.SilhouetteW.jpg)



#### Silhouette (NCA=1.00)

![](sipu/r15.result8.Silhouette.jpg)
![](sipu/r15.result9.Silhouette.jpg)
![](sipu/r15.result15.Silhouette.jpg)



#### GDunn_d1_D3 (NCA=1.00)

![](sipu/r15.result8.GDunn_d1_D3.jpg)
![](sipu/r15.result9.GDunn_d1_D3.jpg)
![](sipu/r15.result15.GDunn_d1_D3.jpg)



#### GDunn_d1_D2 (NCA=1.00)

![](sipu/r15.result8.GDunn_d1_D2.jpg)
![](sipu/r15.result9.GDunn_d1_D2.jpg)
![](sipu/r15.result15.GDunn_d1_D2.jpg)



#### GDunn_d1_D1 (NCA=1.00)

![](sipu/r15.result8.GDunn_d1_D1.jpg)
![](sipu/r15.result9.GDunn_d1_D1.jpg)
![](sipu/r15.result15.GDunn_d1_D1.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=1.00)

![](sipu/r15.result8.sklearn_spectral_Alaplacian_G5.jpg)
![](sipu/r15.result9.sklearn_spectral_Alaplacian_G5.jpg)
![](sipu/r15.result15.sklearn_spectral_Alaplacian_G5.jpg)



#### sklearn_kmeans (NCA=1.00)

![](sipu/r15.result8.sklearn_kmeans.jpg)
![](sipu/r15.result9.sklearn_kmeans.jpg)
![](sipu/r15.result15.sklearn_kmeans.jpg)



#### sklearn_gm (NCA=1.00)

![](sipu/r15.result8.sklearn_gm.jpg)
![](sipu/r15.result9.sklearn_gm.jpg)
![](sipu/r15.result15.sklearn_gm.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=1.00)

![](sipu/r15.result8.sklearn_birch_T0.01_BF50.jpg)
![](sipu/r15.result9.sklearn_birch_T0.01_BF50.jpg)
![](sipu/r15.result15.sklearn_birch_T0.01_BF50.jpg)



#### CalinskiHarabasz (NCA=1.00)

![](sipu/r15.result8.CalinskiHarabasz.jpg)
![](sipu/r15.result9.CalinskiHarabasz.jpg)
![](sipu/r15.result15.CalinskiHarabasz.jpg)



#### FCPS_HDBSCAN_8 (NCA=1.00)

![](sipu/r15.result8.FCPS_HDBSCAN_8.jpg)
![](sipu/r15.result9.FCPS_HDBSCAN_8.jpg)
![](sipu/r15.result15.FCPS_HDBSCAN_8.jpg)



#### FCPS_Diana (NCA=1.00)

![](sipu/r15.result8.FCPS_Diana.jpg)
![](sipu/r15.result9.FCPS_Diana.jpg)
![](sipu/r15.result15.FCPS_Diana.jpg)



#### FCPS_PAM (NCA=1.00)

![](sipu/r15.result8.FCPS_PAM.jpg)
![](sipu/r15.result9.FCPS_PAM.jpg)
![](sipu/r15.result15.FCPS_PAM.jpg)



#### HEMST (NCA=1.00)

![](sipu/r15.result8.HEMST.jpg)
![](sipu/r15.result9.HEMST.jpg)
![](sipu/r15.result15.HEMST.jpg)



#### BallHall (NCA=1.00)

![](sipu/r15.result8.BallHall.jpg)
![](sipu/r15.result9.BallHall.jpg)
![](sipu/r15.result15.BallHall.jpg)



#### DaviesBouldin (NCA=1.00)

![](sipu/r15.result8.DaviesBouldin.jpg)
![](sipu/r15.result9.DaviesBouldin.jpg)
![](sipu/r15.result15.DaviesBouldin.jpg)



#### FCPS_HDBSCAN_2 (NCA=1.00)

![](sipu/r15.result8.FCPS_HDBSCAN_2.jpg)
![](sipu/r15.result9.FCPS_HDBSCAN_2.jpg)
![](sipu/r15.result15.FCPS_HDBSCAN_2.jpg)



#### FCPS_HDBSCAN_4 (NCA=1.00)

![](sipu/r15.result8.FCPS_HDBSCAN_4.jpg)
![](sipu/r15.result9.FCPS_HDBSCAN_4.jpg)
![](sipu/r15.result15.FCPS_HDBSCAN_4.jpg)



#### FCPS_MinEnergy (NCA=1.00)

![](sipu/r15.result8.FCPS_MinEnergy.jpg)
![](sipu/r15.result9.FCPS_MinEnergy.jpg)
![](sipu/r15.result15.FCPS_MinEnergy.jpg)



#### FCPS_Minimax (NCA=1.00)

![](sipu/r15.result8.FCPS_Minimax.jpg)
![](sipu/r15.result9.FCPS_Minimax.jpg)
![](sipu/r15.result15.FCPS_Minimax.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=1.00)

![](sipu/r15.result8.FCPS_AdaptiveDensityPeak.jpg)
![](sipu/r15.result9.FCPS_AdaptiveDensityPeak.jpg)
![](sipu/r15.result15.FCPS_AdaptiveDensityPeak.jpg)



#### fastcluster_weighted (NCA=1.00)

![](sipu/r15.result8.fastcluster_weighted.jpg)
![](sipu/r15.result9.fastcluster_weighted.jpg)
![](sipu/r15.result15.fastcluster_weighted.jpg)



#### fastcluster_ward (NCA=1.00)

![](sipu/r15.result8.fastcluster_ward.jpg)
![](sipu/r15.result9.fastcluster_ward.jpg)
![](sipu/r15.result15.fastcluster_ward.jpg)



#### fastcluster_median (NCA=1.00)

![](sipu/r15.result8.fastcluster_median.jpg)
![](sipu/r15.result9.fastcluster_median.jpg)
![](sipu/r15.result15.fastcluster_median.jpg)



#### fastcluster_complete (NCA=1.00)

![](sipu/r15.result8.fastcluster_complete.jpg)
![](sipu/r15.result9.fastcluster_complete.jpg)
![](sipu/r15.result15.fastcluster_complete.jpg)



#### fastcluster_centroid (NCA=1.00)

![](sipu/r15.result8.fastcluster_centroid.jpg)
![](sipu/r15.result9.fastcluster_centroid.jpg)
![](sipu/r15.result15.fastcluster_centroid.jpg)



#### fastcluster_average (NCA=1.00)

![](sipu/r15.result8.fastcluster_average.jpg)
![](sipu/r15.result9.fastcluster_average.jpg)
![](sipu/r15.result15.fastcluster_average.jpg)



#### Genie_G1.0 (NCA=1.00)

![](sipu/r15.result8.Genie_G1.0.jpg)
![](sipu/r15.result9.Genie_G1.0.jpg)
![](sipu/r15.result15.Genie_G1.0.jpg)



#### Genie_G0.7 (NCA=1.00)

![](sipu/r15.result8.Genie_G0.7.jpg)
![](sipu/r15.result9.Genie_G0.7.jpg)
![](sipu/r15.result15.Genie_G0.7.jpg)



#### Genie_G0.5 (NCA=1.00)

![](sipu/r15.result8.Genie_G0.5.jpg)
![](sipu/r15.result9.Genie_G0.5.jpg)
![](sipu/r15.result15.Genie_G0.5.jpg)



#### FCPS_Clara (NCA=1.00)

![](sipu/r15.result8.FCPS_Clara.jpg)
![](sipu/r15.result9.FCPS_Clara.jpg)
![](sipu/r15.result15.FCPS_Clara.jpg)



#### DuNN_25_Min_Max (NCA=1.00)

![](sipu/r15.result8.DuNN_25_Min_Max.jpg)
![](sipu/r15.result9.DuNN_25_Min_Max.jpg)
![](sipu/r15.result15.DuNN_25_Min_Max.jpg)



#### DuNN_25_Max_Min (NCA=1.00)

![](sipu/r15.result8.DuNN_25_Max_Min.jpg)
![](sipu/r15.result9.DuNN_25_Max_Min.jpg)
![](sipu/r15.result15.DuNN_25_Max_Min.jpg)



#### DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/r15.result8.DuNN_25_Mean_Mean.jpg)
![](sipu/r15.result9.DuNN_25_Mean_Mean.jpg)
![](sipu/r15.result15.DuNN_25_Mean_Mean.jpg)



#### GDunn_d2_D1 (NCA=1.00)

![](sipu/r15.result8.GDunn_d2_D1.jpg)
![](sipu/r15.result9.GDunn_d2_D1.jpg)
![](sipu/r15.result15.GDunn_d2_D1.jpg)



#### FCPS_Fanny (NCA=1.00)

![](sipu/r15.result8.FCPS_Fanny.jpg)
![](sipu/r15.result15.FCPS_Fanny.jpg)



#### GDunn_d4_D1 (NCA=1.00)

![](sipu/r15.result8.GDunn_d4_D1.jpg)
![](sipu/r15.result9.GDunn_d4_D1.jpg)
![](sipu/r15.result15.GDunn_d4_D1.jpg)



#### GDunn_d3_D1 (NCA=0.99)

![](sipu/r15.result8.GDunn_d3_D1.jpg)
![](sipu/r15.result9.GDunn_d3_D1.jpg)
![](sipu/r15.result15.GDunn_d3_D1.jpg)



#### ITM (NCA=0.99)

![](sipu/r15.result8.ITM.jpg)
![](sipu/r15.result9.ITM.jpg)
![](sipu/r15.result15.ITM.jpg)



#### Genie_G0.1 (NCA=0.99)

![](sipu/r15.result8.Genie_G0.1.jpg)
![](sipu/r15.result9.Genie_G0.1.jpg)
![](sipu/r15.result15.Genie_G0.1.jpg)



#### Genie_G0.3 (NCA=0.99)

![](sipu/r15.result8.Genie_G0.3.jpg)
![](sipu/r15.result9.Genie_G0.3.jpg)
![](sipu/r15.result15.Genie_G0.3.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.99)

![](sipu/r15.result8.mst_divisive_CalinskiHarabasz.jpg)
![](sipu/r15.result9.mst_divisive_CalinskiHarabasz.jpg)
![](sipu/r15.result15.mst_divisive_CalinskiHarabasz.jpg)



#### GIc (NCA=0.99)

![](sipu/r15.result8.GIc.jpg)
![](sipu/r15.result9.GIc.jpg)
![](sipu/r15.result15.GIc.jpg)



#### GDunn_d4_D3 (NCA=0.99)

![](sipu/r15.result8.GDunn_d4_D3.jpg)
![](sipu/r15.result9.GDunn_d4_D3.jpg)
![](sipu/r15.result15.GDunn_d4_D3.jpg)



#### GDunn_d4_D2 (NCA=0.99)

![](sipu/r15.result8.GDunn_d4_D2.jpg)
![](sipu/r15.result9.GDunn_d4_D2.jpg)
![](sipu/r15.result15.GDunn_d4_D2.jpg)



#### GDunn_d3_D2 (NCA=0.98)

![](sipu/r15.result8.GDunn_d3_D2.jpg)
![](sipu/r15.result9.GDunn_d3_D2.jpg)
![](sipu/r15.result15.GDunn_d3_D2.jpg)



#### CTCEHC (NCA=0.98)

![](sipu/r15.result8.CTCEHC.jpg)
![](sipu/r15.result9.CTCEHC.jpg)
![](sipu/r15.result15.CTCEHC.jpg)



#### mst_divisive_Silhouette (NCA=0.98)

![](sipu/r15.result8.mst_divisive_Silhouette.jpg)
![](sipu/r15.result9.mst_divisive_Silhouette.jpg)
![](sipu/r15.result15.mst_divisive_Silhouette.jpg)



#### GDunn_d3_D3 (NCA=0.97)

![](sipu/r15.result8.GDunn_d3_D3.jpg)
![](sipu/r15.result9.GDunn_d3_D3.jpg)
![](sipu/r15.result15.GDunn_d3_D3.jpg)



#### GDunn_d2_D3 (NCA=0.94)

![](sipu/r15.result8.GDunn_d2_D3.jpg)
![](sipu/r15.result9.GDunn_d2_D3.jpg)
![](sipu/r15.result15.GDunn_d2_D3.jpg)



#### GDunn_d2_D2 (NCA=0.91)

![](sipu/r15.result8.GDunn_d2_D2.jpg)
![](sipu/r15.result9.GDunn_d2_D2.jpg)
![](sipu/r15.result15.GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.90)

![](sipu/r15.result8.mst_divisive_GDunn_d5_D1.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d5_D1.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d5_D1.jpg)



#### FCPS_Hardcl (NCA=0.90)

![](sipu/r15.result8.FCPS_Hardcl.jpg)
![](sipu/r15.result9.FCPS_Hardcl.jpg)
![](sipu/r15.result15.FCPS_Hardcl.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.89)

![](sipu/r15.result8.mst_divisive_GDunn_d2_D1.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d2_D1.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.88)

![](sipu/r15.result8.mst_divisive_GDunn_d5_D2.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d5_D2.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d5_D2.jpg)



#### IcA (NCA=0.87)

![](sipu/r15.result8.IcA.jpg)
![](sipu/r15.result9.IcA.jpg)
![](sipu/r15.result15.IcA.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.87)

![](sipu/r15.result8.mst_divisive_GDunn_d5_D3.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d5_D3.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.86)

![](sipu/r15.result8.mst_divisive_GDunn_d4_D2.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d4_D2.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.86)

![](sipu/r15.result8.mst_divisive_GDunn_d4_D3.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d4_D3.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.85)

![](sipu/r15.result8.mst_divisive_GDunn_d3_D2.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d3_D2.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.83)

![](sipu/r15.result8.mst_divisive_GDunn_d3_D3.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d3_D3.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.75)

![](sipu/r15.result8.mst_divisive_GDunn_d2_D2.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d2_D2.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.75)

![](sipu/r15.result8.mst_divisive_DaviesBouldin.jpg)
![](sipu/r15.result9.mst_divisive_DaviesBouldin.jpg)
![](sipu/r15.result15.mst_divisive_DaviesBouldin.jpg)



#### GDunn_d5_D2 (NCA=0.72)

![](sipu/r15.result8.GDunn_d5_D2.jpg)
![](sipu/r15.result9.GDunn_d5_D2.jpg)
![](sipu/r15.result15.GDunn_d5_D2.jpg)



#### GDunn_d5_D3 (NCA=0.70)

![](sipu/r15.result8.GDunn_d5_D3.jpg)
![](sipu/r15.result9.GDunn_d5_D3.jpg)
![](sipu/r15.result15.GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.68)

![](sipu/r15.result8.mst_divisive_GDunn_d2_D3.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d2_D3.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d2_D3.jpg)



#### GDunn_d5_D1 (NCA=0.67)

![](sipu/r15.result8.GDunn_d5_D1.jpg)
![](sipu/r15.result9.GDunn_d5_D1.jpg)
![](sipu/r15.result15.GDunn_d5_D1.jpg)



#### FCPS_Softcl (NCA=0.64)

![](sipu/r15.result8.FCPS_Softcl.jpg)
![](sipu/r15.result9.FCPS_Softcl.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.47)

![](sipu/r15.result8.mst_divisive_GDunn_d4_D1.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d4_D1.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.34)

![](sipu/r15.result8.mst_divisive_GDunn_d3_D1.jpg)
![](sipu/r15.result9.mst_divisive_GDunn_d3_D1.jpg)
![](sipu/r15.result15.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_SilhouetteW (NCA=0.05)

![](sipu/r15.result8.mst_divisive_SilhouetteW.jpg)
![](sipu/r15.result9.mst_divisive_SilhouetteW.jpg)
![](sipu/r15.result15.mst_divisive_SilhouetteW.jpg)



## sipu/s1 (n=5000, d=2) <a name="s1"></a>

#### mst_divisive_WCNN_25 (NCA=1.00)

![](sipu/s1.result15.mst_divisive_WCNN_25.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.99)

![](sipu/s1.result15.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### sklearn_gm (NCA=0.99)

![](sipu/s1.result15.sklearn_gm.jpg)



#### Genie_G0.3 (NCA=0.99)

![](sipu/s1.result15.Genie_G0.3.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.99)

![](sipu/s1.result15.mst_divisive_DuNN_25_Min_Max.jpg)



#### Genie_G0.1 (NCA=0.99)

![](sipu/s1.result15.Genie_G0.1.jpg)



#### GIc (NCA=0.99)

![](sipu/s1.result15.GIc.jpg)



#### Genie_G0.5 (NCA=0.99)

![](sipu/s1.result15.Genie_G0.5.jpg)



#### FCPS_Clara (NCA=0.99)

![](sipu/s1.result15.FCPS_Clara.jpg)



#### sklearn_kmeans (NCA=0.99)

![](sipu/s1.result15.sklearn_kmeans.jpg)



#### FCPS_Fanny (NCA=0.99)

![](sipu/s1.result15.FCPS_Fanny.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.99)

![](sipu/s1.result15.sklearn_spectral_Alaplacian_G5.jpg)



#### FCPS_Softcl (NCA=0.99)

![](sipu/s1.result15.FCPS_Softcl.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.99)

![](sipu/s1.result15.FCPS_AdaptiveDensityPeak.jpg)



#### FCPS_PAM (NCA=0.99)

![](sipu/s1.result15.FCPS_PAM.jpg)



#### CTCEHC (NCA=0.99)

![](sipu/s1.result15.CTCEHC.jpg)



#### mst_divisive_Silhouette (NCA=0.99)

![](sipu/s1.result15.mst_divisive_Silhouette.jpg)



#### fastcluster_ward (NCA=0.99)

![](sipu/s1.result15.fastcluster_ward.jpg)



#### fastcluster_average (NCA=0.99)

![](sipu/s1.result15.fastcluster_average.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.99)

![](sipu/s1.result15.sklearn_birch_T0.01_BF50.jpg)



#### fastcluster_centroid (NCA=0.99)

![](sipu/s1.result15.fastcluster_centroid.jpg)



#### FCPS_MinEnergy (NCA=0.99)

![](sipu/s1.result15.FCPS_MinEnergy.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.99)

![](sipu/s1.result15.mst_divisive_CalinskiHarabasz.jpg)



#### fastcluster_complete (NCA=0.98)

![](sipu/s1.result15.fastcluster_complete.jpg)



#### FCPS_Minimax (NCA=0.98)

![](sipu/s1.result15.FCPS_Minimax.jpg)



#### mst_divisive_BallHall (NCA=0.97)

![](sipu/s1.result15.mst_divisive_BallHall.jpg)



#### fastcluster_median (NCA=0.88)

![](sipu/s1.result15.fastcluster_median.jpg)



#### IcA (NCA=0.85)

![](sipu/s1.result15.IcA.jpg)



#### Genie_G0.7 (NCA=0.85)

![](sipu/s1.result15.Genie_G0.7.jpg)



#### FCPS_Diana (NCA=0.85)

![](sipu/s1.result15.FCPS_Diana.jpg)



#### ITM (NCA=0.80)

![](sipu/s1.result15.ITM.jpg)



#### fastcluster_weighted (NCA=0.78)

![](sipu/s1.result15.fastcluster_weighted.jpg)



#### FCPS_Hardcl (NCA=0.71)

![](sipu/s1.result15.FCPS_Hardcl.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.69)

![](sipu/s1.result15.mst_divisive_GDunn_d2_D2.jpg)



#### HEMST (NCA=0.68)

![](sipu/s1.result15.HEMST.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.68)

![](sipu/s1.result15.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.63)

![](sipu/s1.result15.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.63)

![](sipu/s1.result15.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.62)

![](sipu/s1.result15.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.52)

![](sipu/s1.result15.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.50)

![](sipu/s1.result15.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.43)

![](sipu/s1.result15.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.43)

![](sipu/s1.result15.mst_divisive_GDunn_d1_D2.jpg)



#### Genie_G1.0 (NCA=0.43)

![](sipu/s1.result15.Genie_G1.0.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.43)

![](sipu/s1.result15.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.43)

![](sipu/s1.result15.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.43)

![](sipu/s1.result15.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.40)

![](sipu/s1.result15.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.39)

![](sipu/s1.result15.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.39)

![](sipu/s1.result15.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.38)

![](sipu/s1.result15.mst_divisive_GDunn_d4_D3.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.36)

![](sipu/s1.result15.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.35)

![](sipu/s1.result15.mst_divisive_GDunn_d4_D1.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.07)

![](sipu/s1.result15.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.06)

![](sipu/s1.result15.mst_divisive_DaviesBouldin.jpg)



#### mst_divisive_SilhouetteW (NCA=0.00)

![](sipu/s1.result15.mst_divisive_SilhouetteW.jpg)



## sipu/s2 (n=5000, d=2) <a name="s2"></a>

#### sklearn_gm (NCA=0.97)

![](sipu/s2.result15.sklearn_gm.jpg)



#### FCPS_Fanny (NCA=0.97)

![](sipu/s2.result15.FCPS_Fanny.jpg)



#### FCPS_PAM (NCA=0.97)

![](sipu/s2.result15.FCPS_PAM.jpg)



#### FCPS_Softcl (NCA=0.97)

![](sipu/s2.result15.FCPS_Softcl.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.97)

![](sipu/s2.result15.FCPS_AdaptiveDensityPeak.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.97)

![](sipu/s2.result15.sklearn_spectral_Alaplacian_G5.jpg)



#### sklearn_kmeans (NCA=0.97)

![](sipu/s2.result15.sklearn_kmeans.jpg)



#### FCPS_Clara (NCA=0.96)

![](sipu/s2.result15.FCPS_Clara.jpg)



#### Genie_G0.3 (NCA=0.95)

![](sipu/s2.result15.Genie_G0.3.jpg)



#### Genie_G0.1 (NCA=0.95)

![](sipu/s2.result15.Genie_G0.1.jpg)



#### fastcluster_average (NCA=0.95)

![](sipu/s2.result15.fastcluster_average.jpg)



#### mst_divisive_BallHall (NCA=0.95)

![](sipu/s2.result15.mst_divisive_BallHall.jpg)



#### fastcluster_ward (NCA=0.95)

![](sipu/s2.result15.fastcluster_ward.jpg)



#### GIc (NCA=0.95)

![](sipu/s2.result15.GIc.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.95)

![](sipu/s2.result15.sklearn_birch_T0.01_BF50.jpg)



#### FCPS_MinEnergy (NCA=0.95)

![](sipu/s2.result15.FCPS_MinEnergy.jpg)



#### CTCEHC (NCA=0.94)

![](sipu/s2.result15.CTCEHC.jpg)



#### mst_divisive_Silhouette (NCA=0.92)

![](sipu/s2.result15.mst_divisive_Silhouette.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.91)

![](sipu/s2.result15.mst_divisive_CalinskiHarabasz.jpg)



#### fastcluster_centroid (NCA=0.90)

![](sipu/s2.result15.fastcluster_centroid.jpg)



#### FCPS_Diana (NCA=0.87)

![](sipu/s2.result15.FCPS_Diana.jpg)



#### ITM (NCA=0.86)

![](sipu/s2.result15.ITM.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.84)

![](sipu/s2.result15.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### fastcluster_complete (NCA=0.83)

![](sipu/s2.result15.fastcluster_complete.jpg)



#### Genie_G0.5 (NCA=0.83)

![](sipu/s2.result15.Genie_G0.5.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.82)

![](sipu/s2.result15.mst_divisive_DuNN_25_Min_Max.jpg)



#### IcA (NCA=0.82)

![](sipu/s2.result15.IcA.jpg)



#### FCPS_Hardcl (NCA=0.80)

![](sipu/s2.result15.FCPS_Hardcl.jpg)



#### fastcluster_median (NCA=0.76)

![](sipu/s2.result15.fastcluster_median.jpg)



#### fastcluster_weighted (NCA=0.75)

![](sipu/s2.result15.fastcluster_weighted.jpg)



#### FCPS_Minimax (NCA=0.74)

![](sipu/s2.result15.FCPS_Minimax.jpg)



#### mst_divisive_WCNN_25 (NCA=0.69)

![](sipu/s2.result15.mst_divisive_WCNN_25.jpg)



#### HEMST (NCA=0.68)

![](sipu/s2.result15.HEMST.jpg)



#### Genie_G0.7 (NCA=0.62)

![](sipu/s2.result15.Genie_G0.7.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.60)

![](sipu/s2.result15.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.59)

![](sipu/s2.result15.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.59)

![](sipu/s2.result15.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.58)

![](sipu/s2.result15.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.57)

![](sipu/s2.result15.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.55)

![](sipu/s2.result15.mst_divisive_GDunn_d2_D1.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.41)

![](sipu/s2.result15.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.35)

![](sipu/s2.result15.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.29)

![](sipu/s2.result15.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.22)

![](sipu/s2.result15.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.22)

![](sipu/s2.result15.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.21)

![](sipu/s2.result15.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.15)

![](sipu/s2.result15.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.14)

![](sipu/s2.result15.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.14)

![](sipu/s2.result15.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.13)

![](sipu/s2.result15.mst_divisive_DaviesBouldin.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.00)

![](sipu/s2.result15.mst_divisive_GDunn_d1_D1.jpg)



#### Genie_G1.0 (NCA=0.00)

![](sipu/s2.result15.Genie_G1.0.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.00)

![](sipu/s2.result15.FCPS_HDBSCAN_2.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.00)

![](sipu/s2.result15.FCPS_HDBSCAN_4.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.00)

![](sipu/s2.result15.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_SilhouetteW (NCA=0.00)

![](sipu/s2.result15.mst_divisive_SilhouetteW.jpg)



## sipu/s3 (n=5000, d=2) <a name="s3"></a>

#### FCPS_PAM (NCA=0.85)

![](sipu/s3.result15.FCPS_PAM.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.85)

![](sipu/s3.result15.FCPS_AdaptiveDensityPeak.jpg)



#### sklearn_gm (NCA=0.85)

![](sipu/s3.result15.sklearn_gm.jpg)



#### FCPS_Softcl (NCA=0.85)

![](sipu/s3.result15.FCPS_Softcl.jpg)



#### sklearn_kmeans (NCA=0.84)

![](sipu/s3.result15.sklearn_kmeans.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.84)

![](sipu/s3.result15.sklearn_spectral_Alaplacian_G5.jpg)



#### FCPS_Clara (NCA=0.84)

![](sipu/s3.result15.FCPS_Clara.jpg)



#### CTCEHC (NCA=0.82)

![](sipu/s3.result15.CTCEHC.jpg)



#### Genie_G0.1 (NCA=0.82)

![](sipu/s3.result15.Genie_G0.1.jpg)



#### GIc (NCA=0.82)

![](sipu/s3.result15.GIc.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.81)

![](sipu/s3.result15.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_Silhouette (NCA=0.81)

![](sipu/s3.result15.mst_divisive_Silhouette.jpg)



#### fastcluster_ward (NCA=0.81)

![](sipu/s3.result15.fastcluster_ward.jpg)



#### FCPS_MinEnergy (NCA=0.80)

![](sipu/s3.result15.FCPS_MinEnergy.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.79)

![](sipu/s3.result15.sklearn_birch_T0.01_BF50.jpg)



#### Genie_G0.3 (NCA=0.76)

![](sipu/s3.result15.Genie_G0.3.jpg)



#### IcA (NCA=0.76)

![](sipu/s3.result15.IcA.jpg)



#### ITM (NCA=0.76)

![](sipu/s3.result15.ITM.jpg)



#### FCPS_Diana (NCA=0.71)

![](sipu/s3.result15.FCPS_Diana.jpg)



#### FCPS_Minimax (NCA=0.70)

![](sipu/s3.result15.FCPS_Minimax.jpg)



#### FCPS_Hardcl (NCA=0.69)

![](sipu/s3.result15.FCPS_Hardcl.jpg)



#### fastcluster_average (NCA=0.66)

![](sipu/s3.result15.fastcluster_average.jpg)



#### Genie_G0.5 (NCA=0.63)

![](sipu/s3.result15.Genie_G0.5.jpg)



#### fastcluster_centroid (NCA=0.63)

![](sipu/s3.result15.fastcluster_centroid.jpg)



#### fastcluster_complete (NCA=0.57)

![](sipu/s3.result15.fastcluster_complete.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.57)

![](sipu/s3.result15.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.54)

![](sipu/s3.result15.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.54)

![](sipu/s3.result15.mst_divisive_GDunn_d2_D2.jpg)



#### fastcluster_median (NCA=0.52)

![](sipu/s3.result15.fastcluster_median.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.51)

![](sipu/s3.result15.mst_divisive_GDunn_d2_D1.jpg)



#### fastcluster_weighted (NCA=0.50)

![](sipu/s3.result15.fastcluster_weighted.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.50)

![](sipu/s3.result15.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.50)

![](sipu/s3.result15.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.47)

![](sipu/s3.result15.mst_divisive_DuNN_25_Min_Max.jpg)



#### Genie_G0.7 (NCA=0.42)

![](sipu/s3.result15.Genie_G0.7.jpg)



#### HEMST (NCA=0.38)

![](sipu/s3.result15.HEMST.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.36)

![](sipu/s3.result15.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.35)

![](sipu/s3.result15.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.35)

![](sipu/s3.result15.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.28)

![](sipu/s3.result15.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.28)

![](sipu/s3.result15.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.28)

![](sipu/s3.result15.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.20)

![](sipu/s3.result15.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.18)

![](sipu/s3.result15.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_BallHall (NCA=0.09)

![](sipu/s3.result15.mst_divisive_BallHall.jpg)



#### mst_divisive_WCNN_25 (NCA=0.03)

![](sipu/s3.result15.mst_divisive_WCNN_25.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.00)

![](sipu/s3.result15.FCPS_HDBSCAN_2.jpg)



#### Genie_G1.0 (NCA=0.00)

![](sipu/s3.result15.Genie_G1.0.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.00)

![](sipu/s3.result15.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.00)

![](sipu/s3.result15.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.00)

![](sipu/s3.result15.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_SilhouetteW (NCA=0.00)

![](sipu/s3.result15.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.00)

![](sipu/s3.result15.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.00)

![](sipu/s3.result15.FCPS_HDBSCAN_8.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.00)

![](sipu/s3.result15.FCPS_HDBSCAN_4.jpg)



## sipu/s4 (n=5000, d=2) <a name="s4"></a>

#### sklearn_gm (NCA=0.79)

![](sipu/s4.result15.sklearn_gm.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.79)

![](sipu/s4.result15.FCPS_AdaptiveDensityPeak.jpg)



#### FCPS_PAM (NCA=0.78)

![](sipu/s4.result15.FCPS_PAM.jpg)



#### FCPS_Softcl (NCA=0.78)

![](sipu/s4.result15.FCPS_Softcl.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.78)

![](sipu/s4.result15.sklearn_spectral_Alaplacian_G5.jpg)



#### sklearn_kmeans (NCA=0.78)

![](sipu/s4.result15.sklearn_kmeans.jpg)



#### FCPS_Clara (NCA=0.77)

![](sipu/s4.result15.FCPS_Clara.jpg)



#### CTCEHC (NCA=0.77)

![](sipu/s4.result15.CTCEHC.jpg)



#### Genie_G0.1 (NCA=0.77)

![](sipu/s4.result15.Genie_G0.1.jpg)



#### GIc (NCA=0.77)

![](sipu/s4.result15.GIc.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.77)

![](sipu/s4.result15.mst_divisive_CalinskiHarabasz.jpg)



#### FCPS_MinEnergy (NCA=0.75)

![](sipu/s4.result15.FCPS_MinEnergy.jpg)



#### Genie_G0.3 (NCA=0.73)

![](sipu/s4.result15.Genie_G0.3.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.73)

![](sipu/s4.result15.sklearn_birch_T0.01_BF50.jpg)



#### FCPS_Hardcl (NCA=0.72)

![](sipu/s4.result15.FCPS_Hardcl.jpg)



#### fastcluster_ward (NCA=0.68)

![](sipu/s4.result15.fastcluster_ward.jpg)



#### IcA (NCA=0.67)

![](sipu/s4.result15.IcA.jpg)



#### ITM (NCA=0.67)

![](sipu/s4.result15.ITM.jpg)



#### FCPS_Diana (NCA=0.66)

![](sipu/s4.result15.FCPS_Diana.jpg)



#### fastcluster_average (NCA=0.59)

![](sipu/s4.result15.fastcluster_average.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.57)

![](sipu/s4.result15.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.57)

![](sipu/s4.result15.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.57)

![](sipu/s4.result15.mst_divisive_GDunn_d2_D1.jpg)



#### FCPS_Minimax (NCA=0.56)

![](sipu/s4.result15.FCPS_Minimax.jpg)



#### fastcluster_centroid (NCA=0.54)

![](sipu/s4.result15.fastcluster_centroid.jpg)



#### Genie_G0.5 (NCA=0.54)

![](sipu/s4.result15.Genie_G0.5.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.53)

![](sipu/s4.result15.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.53)

![](sipu/s4.result15.mst_divisive_GDunn_d2_D2.jpg)



#### fastcluster_complete (NCA=0.52)

![](sipu/s4.result15.fastcluster_complete.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.49)

![](sipu/s4.result15.mst_divisive_GDunn_d5_D1.jpg)



#### fastcluster_median (NCA=0.43)

![](sipu/s4.result15.fastcluster_median.jpg)



#### fastcluster_weighted (NCA=0.42)

![](sipu/s4.result15.fastcluster_weighted.jpg)



#### Genie_G0.7 (NCA=0.38)

![](sipu/s4.result15.Genie_G0.7.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.38)

![](sipu/s4.result15.mst_divisive_GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.37)

![](sipu/s4.result15.mst_divisive_GDunn_d3_D1.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.36)

![](sipu/s4.result15.mst_divisive_GDunn_d4_D2.jpg)



#### HEMST (NCA=0.34)

![](sipu/s4.result15.HEMST.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.32)

![](sipu/s4.result15.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.28)

![](sipu/s4.result15.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.28)

![](sipu/s4.result15.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.27)

![](sipu/s4.result15.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=0.27)

![](sipu/s4.result15.mst_divisive_DuNN_25_Min_Max.jpg)



#### mst_divisive_Silhouette (NCA=0.21)

![](sipu/s4.result15.mst_divisive_Silhouette.jpg)



#### mst_divisive_BallHall (NCA=0.14)

![](sipu/s4.result15.mst_divisive_BallHall.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=0.10)

![](sipu/s4.result15.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_WCNN_25 (NCA=0.09)

![](sipu/s4.result15.mst_divisive_WCNN_25.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.00)

![](sipu/s4.result15.mst_divisive_DaviesBouldin.jpg)



#### mst_divisive_SilhouetteW (NCA=0.00)

![](sipu/s4.result15.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.00)

![](sipu/s4.result15.mst_divisive_GDunn_d1_D1.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=0.00)

![](sipu/s4.result15.mst_divisive_GDunn_d1_D2.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.00)

![](sipu/s4.result15.FCPS_HDBSCAN_2.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=0.00)

![](sipu/s4.result15.mst_divisive_GDunn_d1_D3.jpg)



#### Genie_G1.0 (NCA=0.00)

![](sipu/s4.result15.Genie_G1.0.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.00)

![](sipu/s4.result15.FCPS_HDBSCAN_8.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.00)

![](sipu/s4.result15.FCPS_HDBSCAN_4.jpg)



## sipu/spiral (n=312, d=2) <a name="spiral"></a>

#### Genie_G0.1 (NCA=1.00)

![](sipu/spiral.result3.Genie_G0.1.jpg)



#### GDunn_d1_D3 (NCA=1.00)

![](sipu/spiral.result3.GDunn_d1_D3.jpg)



#### GDunn_d1_D2 (NCA=1.00)

![](sipu/spiral.result3.GDunn_d1_D2.jpg)



#### GDunn_d1_D1 (NCA=1.00)

![](sipu/spiral.result3.GDunn_d1_D1.jpg)



#### DuNN_25_Min_Max (NCA=1.00)

![](sipu/spiral.result3.DuNN_25_Min_Max.jpg)



#### Genie_G0.3 (NCA=1.00)

![](sipu/spiral.result3.Genie_G0.3.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/spiral.result3.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=1.00)

![](sipu/spiral.result3.mst_divisive_DuNN_25_Min_Max.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=1.00)

![](sipu/spiral.result3.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=1.00)

![](sipu/spiral.result3.mst_divisive_GDunn_d1_D2.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=1.00)

![](sipu/spiral.result3.mst_divisive_GDunn_d1_D1.jpg)



#### FCPS_HDBSCAN_4 (NCA=1.00)

![](sipu/spiral.result3.FCPS_HDBSCAN_4.jpg)



#### FCPS_HDBSCAN_2 (NCA=1.00)

![](sipu/spiral.result3.FCPS_HDBSCAN_2.jpg)



#### Genie_G0.5 (NCA=1.00)

![](sipu/spiral.result3.Genie_G0.5.jpg)



#### Genie_G0.7 (NCA=1.00)

![](sipu/spiral.result3.Genie_G0.7.jpg)



#### Genie_G1.0 (NCA=1.00)

![](sipu/spiral.result3.Genie_G1.0.jpg)



#### GIc (NCA=1.00)

![](sipu/spiral.result3.GIc.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.98)

![](sipu/spiral.result3.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.98)

![](sipu/spiral.result3.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.92)

![](sipu/spiral.result3.mst_divisive_GDunn_d5_D1.jpg)



#### IcA (NCA=0.84)

![](sipu/spiral.result3.IcA.jpg)



#### ITM (NCA=0.83)

![](sipu/spiral.result3.ITM.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.71)

![](sipu/spiral.result3.mst_divisive_GDunn_d5_D3.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.68)

![](sipu/spiral.result3.mst_divisive_GDunn_d2_D1.jpg)



#### CTCEHC (NCA=0.51)

![](sipu/spiral.result3.CTCEHC.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.47)

![](sipu/spiral.result3.mst_divisive_GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.38)

![](sipu/spiral.result3.mst_divisive_GDunn_d2_D3.jpg)



#### mst_divisive_Silhouette (NCA=0.36)

![](sipu/spiral.result3.mst_divisive_Silhouette.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.32)

![](sipu/spiral.result3.mst_divisive_CalinskiHarabasz.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.28)

![](sipu/spiral.result3.mst_divisive_GDunn_d3_D2.jpg)



#### GDunn_d5_D2 (NCA=0.28)

![](sipu/spiral.result3.GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.28)

![](sipu/spiral.result3.mst_divisive_GDunn_d3_D3.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.27)

![](sipu/spiral.result3.mst_divisive_GDunn_d3_D1.jpg)



#### GDunn_d5_D1 (NCA=0.27)

![](sipu/spiral.result3.GDunn_d5_D1.jpg)



#### fastcluster_weighted (NCA=0.14)

![](sipu/spiral.result3.fastcluster_weighted.jpg)



#### mst_divisive_WCNN_25 (NCA=0.12)

![](sipu/spiral.result3.mst_divisive_WCNN_25.jpg)



#### HEMST (NCA=0.12)

![](sipu/spiral.result3.HEMST.jpg)



#### WCNN_25 (NCA=0.12)

![](sipu/spiral.result3.WCNN_25.jpg)



#### GDunn_d2_D1 (NCA=0.10)

![](sipu/spiral.result3.GDunn_d2_D1.jpg)



#### FCPS_MinEnergy (NCA=0.09)

![](sipu/spiral.result3.FCPS_MinEnergy.jpg)



#### fastcluster_median (NCA=0.08)

![](sipu/spiral.result3.fastcluster_median.jpg)



#### GDunn_d3_D3 (NCA=0.08)

![](sipu/spiral.result3.GDunn_d3_D3.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=0.07)

![](sipu/spiral.result3.sklearn_birch_T0.01_BF50.jpg)



#### fastcluster_centroid (NCA=0.07)

![](sipu/spiral.result3.fastcluster_centroid.jpg)



#### GDunn_d3_D2 (NCA=0.07)

![](sipu/spiral.result3.GDunn_d3_D2.jpg)



#### GDunn_d3_D1 (NCA=0.07)

![](sipu/spiral.result3.GDunn_d3_D1.jpg)



#### fastcluster_ward (NCA=0.07)

![](sipu/spiral.result3.fastcluster_ward.jpg)



#### DuNN_25_Mean_Mean (NCA=0.06)

![](sipu/spiral.result3.DuNN_25_Mean_Mean.jpg)



#### FCPS_Minimax (NCA=0.06)

![](sipu/spiral.result3.FCPS_Minimax.jpg)



#### GDunn_d4_D2 (NCA=0.06)

![](sipu/spiral.result3.GDunn_d4_D2.jpg)



#### fastcluster_complete (NCA=0.06)

![](sipu/spiral.result3.fastcluster_complete.jpg)



#### GDunn_d5_D3 (NCA=0.06)

![](sipu/spiral.result3.GDunn_d5_D3.jpg)



#### GDunn_d4_D3 (NCA=0.05)

![](sipu/spiral.result3.GDunn_d4_D3.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.05)

![](sipu/spiral.result3.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.05)

![](sipu/spiral.result3.mst_divisive_GDunn_d4_D3.jpg)



#### GDunn_d2_D2 (NCA=0.04)

![](sipu/spiral.result3.GDunn_d2_D2.jpg)



#### GDunn_d4_D1 (NCA=0.04)

![](sipu/spiral.result3.GDunn_d4_D1.jpg)



#### fastcluster_average (NCA=0.04)

![](sipu/spiral.result3.fastcluster_average.jpg)



#### FCPS_Diana (NCA=0.04)

![](sipu/spiral.result3.FCPS_Diana.jpg)



#### DuNN_25_Max_Min (NCA=0.03)

![](sipu/spiral.result3.DuNN_25_Max_Min.jpg)



#### Silhouette (NCA=0.03)

![](sipu/spiral.result3.Silhouette.jpg)



#### FCPS_Fanny (NCA=0.03)

![](sipu/spiral.result3.FCPS_Fanny.jpg)



#### FCPS_Hardcl (NCA=0.03)

![](sipu/spiral.result3.FCPS_Hardcl.jpg)



#### sklearn_gm (NCA=0.03)

![](sipu/spiral.result3.sklearn_gm.jpg)



#### FCPS_Softcl (NCA=0.02)

![](sipu/spiral.result3.FCPS_Softcl.jpg)



#### GDunn_d2_D3 (NCA=0.02)

![](sipu/spiral.result3.GDunn_d2_D3.jpg)



#### FCPS_PAM (NCA=0.02)

![](sipu/spiral.result3.FCPS_PAM.jpg)



#### FCPS_Clara (NCA=0.02)

![](sipu/spiral.result3.FCPS_Clara.jpg)



#### mst_divisive_SilhouetteW (NCA=0.02)

![](sipu/spiral.result3.mst_divisive_SilhouetteW.jpg)



#### BallHall (NCA=0.02)

![](sipu/spiral.result3.BallHall.jpg)



#### mst_divisive_BallHall (NCA=0.02)

![](sipu/spiral.result3.mst_divisive_BallHall.jpg)



#### DaviesBouldin (NCA=0.02)

![](sipu/spiral.result3.DaviesBouldin.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.02)

![](sipu/spiral.result3.FCPS_AdaptiveDensityPeak.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=0.01)

![](sipu/spiral.result3.sklearn_spectral_Alaplacian_G5.jpg)



#### sklearn_kmeans (NCA=0.01)

![](sipu/spiral.result3.sklearn_kmeans.jpg)



#### CalinskiHarabasz (NCA=0.01)

![](sipu/spiral.result3.CalinskiHarabasz.jpg)



#### SilhouetteW (NCA=0.01)

![](sipu/spiral.result3.SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.01)

![](sipu/spiral.result3.mst_divisive_DaviesBouldin.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.01)

![](sipu/spiral.result3.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.01)

![](sipu/spiral.result3.mst_divisive_GDunn_d4_D1.jpg)



## sipu/unbalance (n=6500, d=2) <a name="unbalance"></a>

#### sklearn_kmeans (NCA=1.00)

![](sipu/unbalance.result8.sklearn_kmeans.jpg)



#### FCPS_PAM (NCA=1.00)

![](sipu/unbalance.result8.FCPS_PAM.jpg)



#### WCNN_25 (NCA=1.00)

![](sipu/unbalance.result8.WCNN_25.jpg)



#### sklearn_gm (NCA=1.00)

![](sipu/unbalance.result8.sklearn_gm.jpg)



#### fastcluster_median (NCA=1.00)

![](sipu/unbalance.result8.fastcluster_median.jpg)



#### BallHall (NCA=1.00)

![](sipu/unbalance.result8.BallHall.jpg)



#### CalinskiHarabasz (NCA=1.00)

![](sipu/unbalance.result8.CalinskiHarabasz.jpg)



#### GDunn_d1_D2 (NCA=1.00)

![](sipu/unbalance.result8.GDunn_d1_D2.jpg)



#### sklearn_spectral_Alaplacian_G5 (NCA=1.00)

![](sipu/unbalance.result8.sklearn_spectral_Alaplacian_G5.jpg)



#### GDunn_d1_D1 (NCA=1.00)

![](sipu/unbalance.result8.GDunn_d1_D1.jpg)



#### mst_divisive_WCNN_25 (NCA=1.00)

![](sipu/unbalance.result8.mst_divisive_WCNN_25.jpg)



#### fastcluster_average (NCA=1.00)

![](sipu/unbalance.result8.fastcluster_average.jpg)



#### DuNN_25_Min_Max (NCA=1.00)

![](sipu/unbalance.result8.DuNN_25_Min_Max.jpg)



#### mst_divisive_DuNN_25_Min_Max (NCA=1.00)

![](sipu/unbalance.result8.mst_divisive_DuNN_25_Min_Max.jpg)



#### mst_divisive_DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/unbalance.result8.mst_divisive_DuNN_25_Mean_Mean.jpg)



#### mst_divisive_GDunn_d1_D3 (NCA=1.00)

![](sipu/unbalance.result8.mst_divisive_GDunn_d1_D3.jpg)



#### mst_divisive_GDunn_d1_D2 (NCA=1.00)

![](sipu/unbalance.result8.mst_divisive_GDunn_d1_D2.jpg)



#### GDunn_d1_D3 (NCA=1.00)

![](sipu/unbalance.result8.GDunn_d1_D3.jpg)



#### FCPS_Clara (NCA=1.00)

![](sipu/unbalance.result8.FCPS_Clara.jpg)



#### Genie_G0.7 (NCA=1.00)

![](sipu/unbalance.result8.Genie_G0.7.jpg)



#### fastcluster_centroid (NCA=1.00)

![](sipu/unbalance.result8.fastcluster_centroid.jpg)



#### fastcluster_ward (NCA=1.00)

![](sipu/unbalance.result8.fastcluster_ward.jpg)



#### FCPS_Minimax (NCA=1.00)

![](sipu/unbalance.result8.FCPS_Minimax.jpg)



#### FCPS_MinEnergy (NCA=1.00)

![](sipu/unbalance.result8.FCPS_MinEnergy.jpg)



#### sklearn_birch_T0.01_BF50 (NCA=1.00)

![](sipu/unbalance.result8.sklearn_birch_T0.01_BF50.jpg)



#### CTCEHC (NCA=1.00)

![](sipu/unbalance.result8.CTCEHC.jpg)



#### mst_divisive_BallHall (NCA=1.00)

![](sipu/unbalance.result8.mst_divisive_BallHall.jpg)



#### DuNN_25_Mean_Mean (NCA=1.00)

![](sipu/unbalance.result8.DuNN_25_Mean_Mean.jpg)



#### mst_divisive_CalinskiHarabasz (NCA=0.93)

![](sipu/unbalance.result8.mst_divisive_CalinskiHarabasz.jpg)



#### GDunn_d4_D2 (NCA=0.92)

![](sipu/unbalance.result8.GDunn_d4_D2.jpg)



#### GDunn_d4_D3 (NCA=0.92)

![](sipu/unbalance.result8.GDunn_d4_D3.jpg)



#### GDunn_d5_D3 (NCA=0.86)

![](sipu/unbalance.result8.GDunn_d5_D3.jpg)



#### fastcluster_weighted (NCA=0.86)

![](sipu/unbalance.result8.fastcluster_weighted.jpg)



#### mst_divisive_GDunn_d1_D1 (NCA=0.86)

![](sipu/unbalance.result8.mst_divisive_GDunn_d1_D1.jpg)



#### FCPS_HDBSCAN_2 (NCA=0.86)

![](sipu/unbalance.result8.FCPS_HDBSCAN_2.jpg)



#### Genie_G1.0 (NCA=0.86)

![](sipu/unbalance.result8.Genie_G1.0.jpg)



#### HEMST (NCA=0.86)

![](sipu/unbalance.result8.HEMST.jpg)



#### GDunn_d3_D1 (NCA=0.85)

![](sipu/unbalance.result8.GDunn_d3_D1.jpg)



#### GDunn_d4_D1 (NCA=0.85)

![](sipu/unbalance.result8.GDunn_d4_D1.jpg)



#### GDunn_d2_D1 (NCA=0.85)

![](sipu/unbalance.result8.GDunn_d2_D1.jpg)



#### GDunn_d3_D2 (NCA=0.85)

![](sipu/unbalance.result8.GDunn_d3_D2.jpg)



#### GDunn_d2_D3 (NCA=0.84)

![](sipu/unbalance.result8.GDunn_d2_D3.jpg)



#### GDunn_d3_D3 (NCA=0.84)

![](sipu/unbalance.result8.GDunn_d3_D3.jpg)



#### fastcluster_complete (NCA=0.80)

![](sipu/unbalance.result8.fastcluster_complete.jpg)



#### mst_divisive_GDunn_d3_D1 (NCA=0.79)

![](sipu/unbalance.result8.mst_divisive_GDunn_d3_D1.jpg)



#### GDunn_d2_D2 (NCA=0.76)

![](sipu/unbalance.result8.GDunn_d2_D2.jpg)



#### mst_divisive_GDunn_d5_D1 (NCA=0.73)

![](sipu/unbalance.result8.mst_divisive_GDunn_d5_D1.jpg)



#### mst_divisive_GDunn_d4_D1 (NCA=0.73)

![](sipu/unbalance.result8.mst_divisive_GDunn_d4_D1.jpg)



#### mst_divisive_GDunn_d5_D2 (NCA=0.71)

![](sipu/unbalance.result8.mst_divisive_GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d5_D3 (NCA=0.71)

![](sipu/unbalance.result8.mst_divisive_GDunn_d5_D3.jpg)



#### Silhouette (NCA=0.70)

![](sipu/unbalance.result8.Silhouette.jpg)



#### FCPS_Diana (NCA=0.69)

![](sipu/unbalance.result8.FCPS_Diana.jpg)



#### mst_divisive_DuNN_25_Max_Min (NCA=0.60)

![](sipu/unbalance.result8.mst_divisive_DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d2_D3 (NCA=0.59)

![](sipu/unbalance.result8.mst_divisive_GDunn_d2_D3.jpg)



#### FCPS_Softcl (NCA=0.58)

![](sipu/unbalance.result8.FCPS_Softcl.jpg)



#### FCPS_HDBSCAN_4 (NCA=0.57)

![](sipu/unbalance.result8.FCPS_HDBSCAN_4.jpg)



#### mst_divisive_Silhouette (NCA=0.57)

![](sipu/unbalance.result8.mst_divisive_Silhouette.jpg)



#### mst_divisive_GDunn_d4_D2 (NCA=0.57)

![](sipu/unbalance.result8.mst_divisive_GDunn_d4_D2.jpg)



#### mst_divisive_GDunn_d3_D2 (NCA=0.57)

![](sipu/unbalance.result8.mst_divisive_GDunn_d3_D2.jpg)



#### mst_divisive_GDunn_d3_D3 (NCA=0.56)

![](sipu/unbalance.result8.mst_divisive_GDunn_d3_D3.jpg)



#### DuNN_25_Max_Min (NCA=0.54)

![](sipu/unbalance.result8.DuNN_25_Max_Min.jpg)



#### mst_divisive_GDunn_d2_D2 (NCA=0.47)

![](sipu/unbalance.result8.mst_divisive_GDunn_d2_D2.jpg)



#### FCPS_HDBSCAN_8 (NCA=0.43)

![](sipu/unbalance.result8.FCPS_HDBSCAN_8.jpg)



#### mst_divisive_GDunn_d2_D1 (NCA=0.42)

![](sipu/unbalance.result8.mst_divisive_GDunn_d2_D1.jpg)



#### FCPS_AdaptiveDensityPeak (NCA=0.41)

![](sipu/unbalance.result8.FCPS_AdaptiveDensityPeak.jpg)



#### GDunn_d5_D2 (NCA=0.39)

![](sipu/unbalance.result8.GDunn_d5_D2.jpg)



#### mst_divisive_GDunn_d4_D3 (NCA=0.36)

![](sipu/unbalance.result8.mst_divisive_GDunn_d4_D3.jpg)



#### Genie_G0.5 (NCA=0.35)

![](sipu/unbalance.result8.Genie_G0.5.jpg)



#### FCPS_Fanny (NCA=0.34)

![](sipu/unbalance.result8.FCPS_Fanny.jpg)



#### GDunn_d5_D1 (NCA=0.29)

![](sipu/unbalance.result8.GDunn_d5_D1.jpg)



#### Genie_G0.3 (NCA=0.29)

![](sipu/unbalance.result8.Genie_G0.3.jpg)



#### DaviesBouldin (NCA=0.27)

![](sipu/unbalance.result8.DaviesBouldin.jpg)



#### FCPS_Hardcl (NCA=0.26)

![](sipu/unbalance.result8.FCPS_Hardcl.jpg)



#### IcA (NCA=0.26)

![](sipu/unbalance.result8.IcA.jpg)



#### GIc (NCA=0.24)

![](sipu/unbalance.result8.GIc.jpg)



#### Genie_G0.1 (NCA=0.24)

![](sipu/unbalance.result8.Genie_G0.1.jpg)



#### ITM (NCA=0.22)

![](sipu/unbalance.result8.ITM.jpg)



#### SilhouetteW (NCA=0.01)

![](sipu/unbalance.result8.SilhouetteW.jpg)



#### mst_divisive_SilhouetteW (NCA=0.01)

![](sipu/unbalance.result8.mst_divisive_SilhouetteW.jpg)



#### mst_divisive_DaviesBouldin (NCA=0.01)

![](sipu/unbalance.result8.mst_divisive_DaviesBouldin.jpg)



## sipu/worms_2 (n=105600, d=2) <a name="worms_2"></a>

#### Genie_G0.1 (NCA=0.57)

![](sipu/worms_2.result35.Genie_G0.1.jpg)



#### GIc (NCA=0.57)

![](sipu/worms_2.result35.GIc.jpg)



#### IcA (NCA=0.55)

![](sipu/worms_2.result35.IcA.jpg)



#### ITM (NCA=0.52)

![](sipu/worms_2.result35.ITM.jpg)



#### Genie_G0.3 (NCA=0.49)

![](sipu/worms_2.result35.Genie_G0.3.jpg)



#### fastcluster_ward (NCA=0.47)

![](sipu/worms_2.result35.fastcluster_ward.jpg)



#### sklearn_kmeans (NCA=0.46)

![](sipu/worms_2.result35.sklearn_kmeans.jpg)



#### Genie_G0.5 (NCA=0.44)

![](sipu/worms_2.result35.Genie_G0.5.jpg)



#### Genie_G0.7 (NCA=0.30)

![](sipu/worms_2.result35.Genie_G0.7.jpg)



#### fastcluster_median (NCA=0.27)

![](sipu/worms_2.result35.fastcluster_median.jpg)



#### fastcluster_centroid (NCA=0.20)

![](sipu/worms_2.result35.fastcluster_centroid.jpg)



#### Genie_G1.0 (NCA=0.00)

![](sipu/worms_2.result35.Genie_G1.0.jpg)



## sipu/worms_64 (n=105000, d=64) <a name="worms_64"></a>

> **(preview generation suppressed)**


#### Genie_G0.1 (NCA=0.84)




#### GIc (NCA=0.84)




#### IcA (NCA=0.77)




#### sklearn_kmeans (NCA=0.75)




#### ITM (NCA=0.74)




#### fastcluster_ward (NCA=0.73)




#### Genie_G0.3 (NCA=0.70)




#### Genie_G0.5 (NCA=0.00)




#### Genie_G0.7 (NCA=0.00)




#### Genie_G1.0 (NCA=0.00)




#### fastcluster_centroid (NCA=0.00)




#### fastcluster_median (NCA=0.00)




