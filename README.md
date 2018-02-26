# SVR.CLUSTERS
**Clusters post-processing:**
1. Visualization of feature space with 2-d plots per cluster
1. Statistics of clusters (min, max calculation)
1. Linear regression of 2-d feature spaces (eg. 3 combinations for ALOS, SRTM, ASTER GDEMs) per cluster
1. ... . . .etc. etc.
* **Data requirements:** Cluster image and the feature space images derived from related projects (SVR.DEM  _https://github.com/miliaresis/SVR.DEM_ and SVR _https://github.com/miliaresis/SVR_). The cluster image is named MASK.TIF (0 for no-data-mask while 1, 2 ... for cluster classes). The feature space images (eg. pc2, pc3 reconstructed elevations) used in clustering are named 01.tif, 02.tif, 03.tif, etc. etc.
* **The vector data model** inside the SVR.CLUSTERS differs from SVR & SVR.DEM projects, since the first column indicate a) 0 for no-data, and b) 1, 2 ... for cluster classes, while the next columns correspond to image data files (01, 02, 03 ..), for example the residual elevations of ALOS, SRTM, & ASTER GDEMs.

# Table 1. 
The linear regression indicate that perfect 2-d linear relationships exist common for all 2-d pairs per cluster for this particular feature space (ALOS, SRTM, ASTER GDEMS) of the (pc2, pc3) reconstructed (residual) elevations in Zagros Ranges.  Notice also that **a + b = 1**

| X     	| Y     	| a*(x)    	| +b      	| correlation 	| Std. Error 	|
|--------	|--------	|----------	|---------	|-------------	|------------	|
| SRTM   	| ALOS   	| 1.0985   	| -0.0985 	| 1           	| 0          	|
| ASTER  	| ALOS   	| -0.52687 	| 1.52687 	| -1          	| 0          	|
| ASTER  	| SRTM   	| -0.47962 	| 1.47962 	| -1          	| 0          	|


# Table 2. 
Min, max values per cluster for the feature space defined by ALOS, SRTM, ASTER GDEMs.

| NBG      	| ALOS   	|       	| SRTM   	|       	| ASTER  	|       	|
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

# Figure 1. 

2-d feature space per cluster visualization

![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping.png)
