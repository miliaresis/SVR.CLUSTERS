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
* **Publications** *Quantification & evaluation of digital elevation models*
  1. Dimension reduction of multi-dimensional elevation data for DEMs optimization & evaluation (in review)
  1. Miliaresis G., Paraschou Ch.V., 2011. An evaluation of the accuracy of the ASTER GDEM and the role of stack number: A case study of   Nisiros Island, Greece. *Remote Sensing Letters*  2(2):127-135. DOI:10.1080/01431161.2010.503667 
  1. Miliaresis G., Delikaraoglou D., 2009. Effects of Percent Tree Canopy Density and DEM Mis-registration to SRTM/NED Vegetation Height Estimates. *Remote Sensing* 1(2):36-49, DOI:10.3390/rs1020036 
  1. Miliaresis G., 2008. The Landcover Impact on the Aspect/Slope Accuracy Dependence of the SRTM-1 Elevation Data for the Humboldt Range. *Sensors* 8(5):3134-3149. DOI: 10.3390/s8053134. 
  1. Miliaresis G., 2007. An upland object based modeling of the vertical accuracy of the SRTM-1 elevation dataset. *Journal of Spatial Sciences* 52(1):13-29. DOI: 10.1080/14498596.2007.9635097 
  1. Miliaresis G., Paraschou Ch., 2005. Vertical accuracy of the SRTM DTED Level 1 of Crete. *Int. J. of Applied Earth Observation & GeoInformation* 7(1):49-59. DOI: 10.1016/j.jag.2004.12.001 

  **Figure 1.** _Visualization of the 4-d  dimensional ALOS, SRTM, ASTER, NED feature space with 3d pairs of scattergrams_
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping0.jpg)

  **Table 1.** Min max of residual H (pc2, pc3) for ALOS, SRTM, ASTER GDEMs (EGM 96) & NED DTM (NAVD 83).

|         	| ALOS  	|     	| SRTM  	|     	| ASTER  	|       	| NED    	|       	| percent 	|
|---------	|-------	|------	|-------	|------	|--------	|-------	|--------	|-------	|---------	|
| cluster 	| min   	| max  	| min   	| max  	| min    	| max   	| min    	| max   	| %       	|
| 4       	| -41.2 	| 0.1  	| -31.5 	| 0.3  	| 4.5    	| 181   	| -104.8 	| -1    	| 11.2    	|
| 5       	| 0.1   	| 1.7  	| 0.3   	| 1.5  	| -2     	| 4.5   	| -1     	| 2.7   	| 15.2    	|
| 1       	| 1.7   	| 2.6  	| 1.5   	| 2.2  	| -6.1   	| -2    	| 2.7    	| 5.1   	| 16.5    	|
| 6       	| 2.6   	| 3.5  	| 2.2   	| 2.9  	| -9.9   	| -6.1  	| 5.1    	| 7.4   	| 16.1    	|
| 2       	| 3.5   	| 4.6  	| 2.9   	| 3.7  	| -14.4  	| -9.9  	| 7.4    	| 10.1  	| 15.3    	|
| 3       	| 4.6   	| 6.3  	| 3.7   	| 5.1  	| -21.9  	| -14.4 	| 10.1   	| 14.4  	| 15.1    	|
| 7       	| 6.3   	| 56.4 	| 5.1   	| 43.7 	| -235.6 	| -21.9 	| 14.4   	| 140.1 	| 10.5    	|

  **Figure 2.** _Visualization of the 46 dimensional 8-day, 1-km, reconstructed LST_
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping2.jpg)

  **Table 2.** _2-d linear regressions for all data for this particular feature space (ALOS, SRTM, ASTER GDEMS) of the (pc2, pc3) reconstructed (residual) elevations in Zagros Ranges_ 

| X     	| Y    	| a*(x)           	| +b               	| correlation     	| p 	| std.error           	|
|-------	|------	|-----------------	|------------------	|-----------------	|---	|---------------------	|
| SRTM  	| ALOS 	| 1.09396167786   	| -0.0211044935064 	| 0.999949028854  	| 0 	| 0.00000209006029549 	|
| ASTER 	| ALOS 	| -0.546761136998 	| 0.365189686874   	| -0.986233601935 	| 0 	| 0.0000173462688792  	|
| ASTER 	| SRTM 	| -0.498902179662 	| 0.353890206081   	| -0.98451379167  	| 0 	| 0.0000168095510177  	|

  **Table 3.** _The linear regression indicate that perfect 2-d linear relationships exist (common for all 2-d pairs per cluster) for this particular feature space (ALOS, SRTM, ASTER GDEMS) of the (pc2, pc3) reconstructed (residual) elevations in Zagros Ranges.  Notice also that_ **a + b = 1**

| X     	| Y    	| a*(x)           	| +b               	| correlation 	| p 	| std.error                	|
|-------	|------	|-----------------	|------------------	|-------------	|---	|--------------------------	|
| SRTM  	| ALOS 	| 1.09850052619   	| -0.0985005255746 	| 1           	| 0 	| 0.000000000208527943367  	|
| ASTER 	| ALOS 	| -0.526870536393 	| 1.52687053982    	| -1          	| 0 	| 0.0000000000466846053007 	|
| ASTER 	| SRTM 	| -0.479627022318 	| 1.47962702487    	| -1          	| 0 	| 0.0000000000673680778821 	|

  **Figure 3.** _Selected **3d per cluster** scattergrams for the 3-d feature space defined by by residual elevations (pc2,  pc3 reconstructed ALOS, SRTM, ASTER GDEMs)_
![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping_3d.jpg)

  **Table 4.** _Min, max values per cluster for the feature space defined by ALOS, SRTM, ASTER GDEMs_

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

  **Figure 4.** _2-d feature space visualization per cluster for the 3-d feature space defined by residual elevations (pc2,  pc3 reconstructed ALOS, SRTM, ASTER GDEMs)_

![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping.png)

  **Figure 5.** _2-d feature space visualization per cluster for the 4-d feature space defined by residual elevations (pc2,  pc3 reconstructed **ALOS, SRTM, ASTER GDEMs & NED DTM**)_

![Example of output images](https://github.com/miliaresis/SVR.CLUSTERS/blob/master/mapping_4db.jpg)
