# SVR.CLUSTERS
* Visualization &amp; statistics of clusters: **I apply some expiremental processing that after finalisation is included in SVR.DEM** _https://github.com/miliaresis/SVR.DEM_
* Input is the Cluster image (MASK.TIF) as well as the images used in clustering (eg. pc2, pc3 reconstructed DEMS) under the naming convention 01.tif, 02.tif, 03.tif, etc. etc.
* The vector data model differs from SVR & SVR.DEM, since the first column indicate 0 for no-data, 1, 2 ... for cluster classes 
while the next columns correspond to image data files (01, 02 ..), for example residual elevations of ALOS, SRTM, ASTER ...

# Data
  * Multi-(3-d) dimensional (ALOS {median}, SRTM, ASTER) DEM of SE Zagros Ranges, Mendeley Data, v.11, _**http://dx.doi.org/10.17632/bswsr3gpy2.11**_ (see file clusters_feature_space_visualization.zip)

![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping.png)
