# SVR.CLUSTERS
* Visualization &amp; statistics of clusters: **I apply some expiremental processing that after finalisation is included in SVR.DEM** _https://github.com/miliaresis/SVR.DEM_
* Input is the Cluster image (MASK.TIF) as well as the images used in clustering (eg. pc2, pc3 reconstructed DEMS) under the naming convention 01.tif, 02.tif, 03.tif, etc. etc.
* The vector data model inside the SVR.CLUSTERS differs from SVR & SVR.DEM projects, since the first column indicate a) 0 for no-data, and b) 1, 2 ... for cluster classes, while the next columns correspond to image data files (01, 02, 03 ..), for example the residual elevations of ALOS, SRTM, ASTER.

![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping.png)
