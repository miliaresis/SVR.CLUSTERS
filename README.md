# SVR.CLUSTERS
* Visualization of feature space with 2-d plots per cluster &amp; statistics of clusters: **expiremental processing is applied that after finalisation is included in other projects, for example SVR.DEM** _https://github.com/miliaresis/SVR.DEM_
* Input is the Cluster image (MASK.TIF) as well as the images used in clustering (eg. pc2, pc3 reconstructed DEMS) under the naming convention 01.tif, 02.tif, 03.tif, etc. etc.
* The vector data model inside the SVR.CLUSTERS differs from SVR & SVR.DEM projects, since the first column indicate a) 0 for no-data, and b) 1, 2 ... for cluster classes, while the next columns correspond to image data files (01, 02, 03 ..), for example the residual elevations of ALOS, SRTM, & ASTER GDEMs.

| NBG      	| ALOS   	| ALOS  	| SRTM   	| SRTM  	| ASTER  	| ASTER 	|
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

![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping.png)
