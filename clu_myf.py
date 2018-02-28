# -*- coding: utf-8 -*-
"""
Created on  17th of Jan., 2018

@author: gmiliar (George Ch. Miliaresis)
Analyze/model clusters(SVR.CLASSES) by G.Ch. Miliaresis
Ver. 2017.02 winpython implementation, (https://winpython.github.io/)
Details in https://github.com/miliaresis
           https://sites.google.com/site/miliaresisg/
"""
import numpy as np


def Processing_constants():
    """ TIF import options (in function tiff_to_np in dim_myf)
              if PIL  then Image from PIL is used
              if SKITimage  then skimage.io is used """
    print('__________________________________________________________________')
    print('\n --- Cluster visualization & analysis by G. Ch. Miliaresis ---\n')
    print('   Vector data model differs from SVR & SVR.DEM')
    print('      MASK [0=no data, >1 for cluster classes], 01, 02,... for the')
    print('      feature images (eg. residual H for ALOS, SRTM, ASTER)')
    tiff_import_options = ['PIL', 'SKITimage']
    print('   TIFF import options', tiff_import_options)
    print('__________________________________________________________________')
    print('\nDISPLAY ACTIVE DATA HEADER')
    return tiff_import_options


def filenames_of_images(k):
    """ Defines the filenames of images  MASK, 01, 02, 03 .... """
    a = '0'
    Lfiles = ['MASK']
    for i in range(k):
        if i < 9:
            d = a + str(i+1)
        else:
            d = str(i+1)
        Lfiles.append(d)
    return Lfiles


def findcreatenewpath():
    """ Creates a new (non exisiting) path within the data/script-path where
    the output files are stored. The path name is ...\outX where X is
    a number determined automatically by this script
    """
    import os
    oldpath = os.getcwd()
    newpath = oldpath+'\out0'
    i = 0
    while os.path.isdir(newpath) is True:
        i = i + 1
        newpath = oldpath+'\out'+str(i)
    os.makedirs(newpath)
    print('\n Output files path: ', newpath)
    return newpath


def historyfile():
    """ Track (save to file) the user inputs and the file outputs """
    from time import time
    from datetime import date
    f = open('_history.txt', 'w')
    f.write('\n date: ' + str(date.today()) + ' time = ' + str(time()))
    f.write('\n _history.txt tracks user selections & output files')
    return f


def input_screen_int(xstring, xmin, xmax):
    """ input an integer X from screen in the range min<=X<=xmax """
    yy = xstring + ' in [' + str(xmin) + ', ' + str(xmax) + ']: '
    X = xmin-1
    while (X < xmin) or (X > xmax):
        X = int(input(yy))
    return X


def input_screen_str_yn(xstring):
    """ input a string X from screen y, Y, n, N """
    yy = xstring + '(y, Y, n, N) : '
    X = 'y '
    while (X != 'y') and (X != 'Y') and (X != 'n') and (X != 'N'):
        X = input(yy)
    return X


def dummyvar_fcheck():
    """ assign dummy variables if file donot exist (to exit from return var """
    imarray = np.zeros(shape=(3, 3))
    rows = 3
    cols = 3
    continue1 = 'no'
    return imarray, rows, cols, continue1


def data_imv_read(LfilesDIR, featuredimension, T):
    """Main Data FILE (individual images read) """
    print('__________________________________________________________________')
    print('\nIMPORT/READ DATA FILES')
    Lfiles = filenames_of_images(featuredimension)
    LfilesEXTENSION = '.tif'
    print('\nFiles EXTENSION= ', LfilesEXTENSION, 'DIR: ', LfilesDIR, '\n')
    print('FILENAMES: ', Lfiles, ' (names are case sensitive)\n')
    for i in range(len(Lfiles)):
        Lfiles[i] = LfilesDIR + "\\" + Lfiles[i] + LfilesEXTENSION
    data, row, col, continue1 = readimagetiff(Lfiles, T)
    return data, row, col, continue1


def tiff_to_np(filename, T):
    """Read/Import tiff file """
    if T == 'PIL':
        from PIL import Image
        img = Image.open(filename)
        im2 = np.array(img)
        img.close()
    if T == 'SKITimage':
        from skimage.io import imread
        im2 = imread(filename)
    return im2


def readdatafiles0(filename, continue1, T):
    """Read image 2-d tif file &  convert it 1-d to numpy array """
    import os.path
    if continue1 == 'yes':
        if os.path.isfile(filename):
            im2 = tiff_to_np(filename, T)
            imarray = im2.reshape(im2.shape[0] * im2.shape[1])
            print(filename, im2.shape)
            rows = im2.shape[0]
            cols = im2.shape[1]
        else:
            print(filename, ' do not exist')
            imarray, rows, cols, continue1 = dummyvar_fcheck()
    return imarray, rows, cols, continue1


def readdatafiles(filename, rows1, cols1, continue1, T):
    """Read SVR 2-d tif file &  convert it 1-dto numpy array """
    import os.path
    if continue1 == 'yes':
        if os.path.isfile(filename):
            im2 = tiff_to_np(filename, T)
            imarray = im2.reshape(im2.shape[0] * im2.shape[1])
            print(filename, im2.shape)
            if filename == '    ':
                print(' ')
            else:
                if rows1 == im2.shape[0] and cols1 == im2.shape[1]:
                    rows = im2.shape[0]
                    cols = im2.shape[1]
                else:
                    imarray, rows, cols, continue1 = dummyvar_fcheck()
                    print(filename, 'rows, cols differ from others')
        else:
            print(filename, ' do not exist')
            imarray, rows, cols, continue1 = dummyvar_fcheck()
    else:
        imarray, rows, cols, continue1 = dummyvar_fcheck()
    return imarray, rows, cols, continue1


def readimagetiff(Ldatafiles, T):
    """Read individual tiff images - convert data"""
    c1 = 'yes'
    img0, rows, cols, c1 = readdatafiles0(Ldatafiles[0], c1, T)
    img = np.zeros(shape=(img0.shape[0], len(Ldatafiles)))
    img[:, 0] = img0[:]
    rows1 = rows
    cols1 = cols
    for k in range(1, len(Ldatafiles)):
        img1, rows, cols, c1 = readdatafiles(Ldatafiles[k], rows1, cols1,
                                             c1, T)
        img[:, k] = img1
    if c1 == 'yes':
        all_data_elements = img0.sum()
        data = np.zeros(shape=(all_data_elements, len(Ldatafiles)))
        print('\n      Vector data dimensions : ', data.shape)
        m = -1
        for i in range(img0.shape[0]):
            if img0[i] >= 0:
                m = m + 1
                data[m, 0] = img0[i]
                for k in range(1, len(Ldatafiles)):
                    data[m, k] = img[i, k]
    else:
        data = np.zeros(shape=(3, 3))
        rows1 = 0
        cols1 = 0
    return data, rows1, cols1, c1


def findpaths_data2csv(data):
    """find newpath to store outputs, change to newpath data dir """
    newpath = findcreatenewpath()
    import os
    oldpath = os.getcwd()
    os.chdir(newpath)
    f = historyfile()
    f.write("""\n\nDimensionality reduction-DEM Selective Variance Reduction by
                George Ch. Miliaresis (https://about.me/miliaresis)
                Details in https://github.com/miliaresis [Repository SVR.DEM]
                https://sites.google.com/site/miliaresisg/ \n""")
    f.write('\n      Output data files are stored to : ' + newpath + '\n')
    return f, oldpath


def create_data_files(data):
    """ Read data file, create sub-matrices"""
    rows, cols = data.shape
    # Create sub-matrices: IDs, H, LAT, LON & LST
    Ids = np.zeros(shape=(rows, 1))
    Ids[:, 0] = data[:, 0]
    LST = np.zeros(shape=(rows, data.shape[1]-1))
    LST = data[:, 1:data.shape[1]]
    return Ids, LST


def define_cluster_matrices(data, k, f):
    """create cluster sub-matrices, k= the specific cluster id """
    cluster_elements = -1
    for i in range(data.shape[0]):
        if data[i, 0] == k:
            cluster_elements = cluster_elements + 1
    file_xxx = '_descriptive' + str(k) + '.xlsx'
    file_xxx2 = '_linear_regression_cluster_' + str(k) + '.xlsx'
    size = cluster_elements + 1
    print('   Cluster: ', k, '  size: ', size, ' ', file_xxx, ' ', file_xxx2)
    f.write('\n' + file_xxx + ' pixels: ' + str(size))
    cluster_matrix = np.zeros(shape=(size, data.shape[1]))
    m = -1
    for i in range(data.shape[0]):
        if data[i, 0] == k:
            m = m + 1
            for l in range(1, data.shape[1]):
                cluster_matrix[m, l] = data[i, l]
    return cluster_matrix, size


def compute_descriptive_stats(RLST, x, cluster_id, size):
    """compute min and max """
    import xlsxwriter
    a = np.zeros(shape=(RLST.shape[1], 3))
    a[:, 0] = RLST.min(axis=0)
    a[:, 1] = RLST.max(axis=0)
    a[:, 2] = size
    y = ['Minimum', 'Maximum', 'pixels']
    file_xxx = '_descriptive' + str(cluster_id) + '.xlsx'
    workbook = xlsxwriter.Workbook(file_xxx)
    worksheet5 = workbook.add_worksheet()
    worksheet5.name = 'descriptives'
    worksheet5.write(0, 0, 'descriptive stats')
    worksheet5.write(0, 1, 'cluster ' + str(cluster_id))
    for i in range(len(y)):
        worksheet5.write(1, i+1, y[i])
    for i in range(len(x)):
        worksheet5.write(i+2, 0, x[i])
    for i in range(a.shape[1]):
        for j in range(a.shape[0]):
            worksheet5.write(j+2, i+1, str(a[j, i]))
    workbook.close()


def Linear_Regression(data2, LL, c_id, f):
    """Linear Regression y = a * x +b """
    from scipy.stats import linregress
    import xlsxwriter
    y = ['X-axis', 'Y-axis', 'a*(x)', '+b', 'correlation', 'p', 'std.error']
    file_xxx = '_linear_regression_cluster_' + str(c_id) + '.xlsx'
    workbook = xlsxwriter.Workbook(file_xxx)
    worksheet5 = workbook.add_worksheet()
    worksheet5.name = 'Linear_regression'
    worksheet5.write(0, 0, 'linear regression')
    worksheet5.write(0, 1, 'cluster ' + str(c_id))
    if (c_id == 0):
        worksheet5.write(0, 1, 'regression for all data')
        file_xxx = '_linear_regression_all_data_' + '.xlsx'
        print('\n Linear regression for all data ', file_xxx, ' \n')
        f.write('\n Linear regression for all data  ' + file_xxx)
    for i in range(len(y)):
        worksheet5.write(1, i+1, y[i])
    k = data2.shape[1]
    ss = 0
    for i in range(k):
        for l in range(k):
            if i > l:
                X = np.zeros(shape=(data2.shape[0], 2))
                X[:, 0] = data2[:, i]
                X[:, 1] = data2[:, l]
                slope, intercept, r_value, p_value, std_err = linregress(X)
                y[0] = LL[i]
                y[1] = LL[l]
                y[2] = str(slope)
                y[3] = str(intercept)
                y[4] = str(r_value)
                y[5] = str(p_value)
                y[6] = str(std_err)
                ss = ss + 1
                for kkk in range(len(y)):
                    worksheet5.write(ss+2, kkk+1, y[kkk])
    workbook.close()


def scatter_2d_plots(data2, LL, c_id, f):
    """ Display 2d scatter plots of the feature space per cluster """
    import matplotlib.pyplot as plt
    k = data2.shape[1]
    for i in range(k):
        for l in range(k):
            if i > l:
                title = "cluster_" + str(c_id) + "_" + LL[i] + "_" + LL[l]
                plt.figure()
                plt.title("cluster: " + str(c_id))
                plt.scatter(data2[:, i], data2[:, l], 1, marker="+")
                plt.xlabel(LL[i])
                plt.ylabel(LL[l])
                plt.savefig(title + '.png', dpi=300)
                plt.show()
                plt.close("all")


def linear_Regression_of_all_data(data, LL, c_id, f):
    """Compute linear regression of all data """
    data2 = np.zeros(shape=(data.shape[0], data.shape[1]-1))
    data2 = data[:, 1:data.shape[1]]
    Linear_Regression(data2, LL, c_id, f)


def scatter_3d(data2, LL, c_id, f):
    """3d-scatergram per cluster """
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    title = "cluster " + str(c_id)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title(title)
    x = data2[:, 2]
    y = data2[:, 1]
    z = data2[:, 0]
    ax.scatter(x, y, z, s=1, marker='+')
    ax.set_xlabel(LL[2])
    ax.set_ylabel(LL[1])
    ax.set_zlabel(LL[0])
    plt.savefig("_plot3d_"+title+'.png', dpi=300)
    plt.show()
    plt.close("all")


def descriptive_stats(data, LABELmonths3, f):
    """Cluster stats main calls """
    f.write('\n Display 2-d feature space components per cluster')
    f.write('\n Compute linear regression per 2-d features per cluster')
    f.write('\n Display 3-d feature space components per cluster')
    print('\n Compute min, max stats, linear regression per 2-d features and ',
          'feature space 2-d as well as 3-d plots (if dim = 3)  per cluster')
    linear_Regression_of_all_data(data, LABELmonths3, 0, f)
    No_of_clusters = data[:, 0].max(axis=0)
    for cluster_id in range(1, int(No_of_clusters)+1):
        datacluster, size = define_cluster_matrices(data, cluster_id, f)
        data2 = datacluster[:, 1:datacluster.shape[1]]
        compute_descriptive_stats(data2, LABELmonths3, cluster_id, size)
        scatter_2d_plots(data2, LABELmonths3, cluster_id, f)
        Linear_Regression(data2, LABELmonths3, cluster_id, f)
        scatter_3d(data2, LABELmonths3, cluster_id, f)


def MainRun(data, rows, cols, GeoExtent, FigureLabels, LabelLST, LabelLSTxls,
            Hmin, Hmax):
    """ Main run module of SVR_CLU.py"""
    f, oldpath = findpaths_data2csv(data)
    xyxstr = 'Display 2-d feature space per cluster ? '
    Display_yesno2 = input_screen_str_yn(xyxstr)
    if Display_yesno2 == 'Y' or Display_yesno2 == 'y':
        f.write('\n Display 2-d feature space')
        descriptive_stats(data, LabelLSTxls, f)
    f.close()
    from os import chdir
    chdir(oldpath)
