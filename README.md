# SVR.CLUSTERS
* **Clusters post-processing,** A win python program (https://winpython.github.io/) consisting of 3 modules **clu_r.py** and the 2 library MODULEs **clu_data_headers**, & **clu_myf.py**, that perform:
  1. Visualization of feature space with 2-d plots per cluster
  1. Visualization of feature space with 3-d plots per cluster
  1. Statistics of clusters (min, max calculation)
  1. Linear regression of 2-d feature spaces (eg. 3 combinations for ALOS, SRTM, ASTER GDEMs) per cluster
* **Video:** _https://vimeo.com/258236125_
* **Data:** Cluster image and the feature space images derived from related projects (SVR & SVR.DEM). The cluster image is named MASK.TIF (0= no data, 1, 2 ... for cluster classes). The feature space images (eg. pc2, pc3 reconstructed elevations) used in clustering are named 01.tif, 02.tif, etc. **The vector data model** in SVR.CLUSTERS differs from SVR & SVR.DEM projects, since the first column indicate a) 0 for no-data, and b) 1, 2 ... for cluster classes, while the next columns correspond to image data files (01, 02, 03 ..), for example the residual elevations of ALOS, SRTM, ASTER GDEMs.
  * Miliaresis, G. 2018. **3-d feature space (residual elevations of ALOS, SRTM, ASTER, GDEMs)**  & cluster image (datacl4) for the enlarged study area (data4) of SE Zagros Ranges. Mendeley Data, v.1, **_http://dx.doi.org/10.17632/rhw75rh6xk.1_** Related project SVR.DEM
  * Miliaresis, G. 2018. **4-d feature space (residual elevations of ALOS, SRTM, ASTER GDEMs & NED DTM)** & cluster image (datacl2) for the Death Valley, SW USA (data2). Mendeley Data, v.1, **_http://dx.doi.org/10.17632/3jmcw6fggt.1_** Related project SVR.DEM
  * Miliaresis, G. 2018. **46-d feature space (1-km, 8-day, of SVR-LST data)** & cluster image (SW USA). Mendeley Data. v.1,  **_http://dx.doi.org/10.17632/zt9rzv9bwt.1_** Related project SVR (LST)
# Case studies
  * **A. 4-d feature space** (just for testing & visualization since the vertical datums differ)  
  
   **Table a1.** _Min max statistics for the 7 clusters._  
  
  |         	| ALOS  	|   (m)	| SRTM  	|   (m)	| ASTER  	|   (m)  	| NED    	|  (m)   	| percent 	|
  |---------	|-------	|------	|-------	|------	|--------	|-------	|--------	|-------	|---------	|
  | cluster 	| min   	| max  	| min   	| max  	| min    	| max   	| min    	| max   	| %       	|
  | 4       	| -41.2 	| 0.1  	| -31.5 	| 0.3  	| 4.5    	| 181   	| -104.8 	| -1    	| 11.2    	|
  | 5       	| 0.1   	| 1.7  	| 0.3   	| 1.5  	| -2     	| 4.5   	| -1     	| 2.7   	| 15.2    	|
  | 1       	| 1.7   	| 2.6  	| 1.5   	| 2.2  	| -6.1   	| -2    	| 2.7    	| 5.1   	| 16.5    	|
  | 6       	| 2.6   	| 3.5  	| 2.2   	| 2.9  	| -9.9   	| -6.1  	| 5.1    	| 7.4   	| 16.1    	|
  | 2       	| 3.5   	| 4.6  	| 2.9   	| 3.7  	| -14.4  	| -9.9  	| 7.4    	| 10.1  	| 15.3    	|
  | 3       	| 4.6   	| 6.3  	| 3.7   	| 5.1  	| -21.9  	| -14.4 	| 10.1   	| 14.4  	| 15.1    	|
  | 7       	| 6.3   	| 56.4 	| 5.1   	| 43.7 	| -235.6 	| -21.9 	| 14.4   	| 140.1 	| 10.5    	|

   **Figure a2.** _2-d feature space visualization (6 combinations) per cluster (7 clusters)_  
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping_4db.jpg)  

   **Figure a3.** _Clusters centroids (7 clusters)_  
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/map_centroids.jpg)  
* **B. 46-d visualization of the 8-day, 1-km, reconstructed LST of the SW USA**  
  **Figure b1.** _Visualization of the reconstructed LST._  
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping2.jpg)

* **C. 3-d visualzation (ALOS, SRTM, ASTER GDEMS) of the (pc2, pc3) reconstructed (residual) elevations in Zagros Ranges**  
  
  **Figure c1.** _Selected 3d scattergrams per cluster._  
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping_3d.jpg)

  **Table c3.** _Min, max statistics per cluster._  

| NBG      	| ALOS   	|    (m)	| SRTM   	|   (m)  	| ASTER  	|    (m) 	|
|----------	|--------	|-------	|--------	|-------	|--------	|-------	|
| Clusters 	| Min    	| Max   	| Min    	| Max   	| Min    	| Max   	|
| 3        	| -183.3 	| -8.2  	| -166.8 	| -7.4  	| 18.5   	| 350.8 	|
| 5        	| -8.2   	| -0.9  	| -7.4   	| -0.7  	| 4.6    	| 18.5  	|
| 6        	| -0.9   	| 1.9   	| -0.7   	| 1.8   	| -0.7   	| 4.6   	|
| 1        	| 1.9    	| 3.7   	| 1.8    	| 3.5   	| -4.2   	| -0.7  	|
| 2        	| 3.7    	| 5.4   	| 3.5    	| 5     	| -7.3   	| -4.2  	|
| 4        	| 5.4    	| 7.5   	| 5      	| 6.9   	| -11.2  	| -7.3  	|
| 7        	| 7.5    	| 13    	| 6.9    	| 11.9  	| -21.8  	| -11.2 	|
| 3        	| 13     	| 335.9 	| 11.9   	| 305.9 	| -634.7 	| -21.8 	|

