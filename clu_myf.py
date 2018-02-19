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


def dem_differences_stdev(R):
    """ Compute st.dev of elevation differences among DEM pairs"""
    data = np.zeros(shape=(R.shape[1], R.shape[1]))
    for i in range(0, R.shape[1]-1):
        for j in range(1, R.shape[1]):
            if j > i:
                data[i, j] = (R[:, i] - R[:, j]).std()
                data[j, i] = data[i, j]
    return data


def dem_differences_absoulte_mean(R):
    """ Compute absolute mean of elevation differences among DEM pairs"""
    data = np.zeros(shape=(R.shape[1], R.shape[1]))
    for i in range(0, R.shape[1]-1):
        for j in range(1, R.shape[1]):
            if j > i:
                data[i, j] = np.absolute((R[:, i] - R[:, j])).mean()
                data[j, i] = data[i, j]
    return data


def dem_differences_mean(R):
    """ Compute mean of elevation differences among DEM pairs"""
    data = np.zeros(shape=(R.shape[1], R.shape[1]))
    for i in range(0, R.shape[1]-1):
        for j in range(1, R.shape[1]):
            if j > i:
                data[i, j] = (R[:, i] - R[:, j]).mean()
                data[j, i] = data[i, j]
    return data


def dem_differences_RMS(R):
    """ Compute RMS of elevation differences among DEM pairs"""
    data = np.zeros(shape=(R.shape[1], R.shape[1]))
    for i in range(0, R.shape[1]-1):
        for j in range(1, R.shape[1]):
            if j > i:
                data[i, j] = np.sqrt((R[:, i] - R[:, j]).T.dot(
                        R[:, i] - R[:, j])/(R.shape[0]-1))
                data[j, i] = data[i, j]
    return data


def compute_descriptive_stats(RLST, x, lst_or_rlst):
    """compute mean, st.dev, kurtosis, skew"""
    from scipy.stats import kurtosis
    from scipy.stats import skew
    import xlsxwriter
    a = np.zeros(shape=(RLST.shape[1], 6))
    a[:, 0] = RLST.min(axis=0)
    a[:, 1] = RLST.max(axis=0)
    a[:, 2] = RLST.mean(axis=0)
    a[:, 3] = RLST.std(axis=0)
    a[:, 4] = skew(RLST, axis=0)
    a[:, 5] = kurtosis(RLST, axis=0)
    y = ['Minimum', 'Maximum', 'Mean', 'St.Dev.', 'Skew', 'Kurtosis']
    if lst_or_rlst == 'RLST':
        print('SAVE descriptive Rdata stats to file: descriptives_RLST.xlsx')
        workbook = xlsxwriter.Workbook('_descriptives_RLST.xlsx')
    else:
        print('SAVE descriptive data stats to file: descriptives_LST.xlsx')
        workbook = xlsxwriter.Workbook('_descriptives_LST.xlsx')
    worksheet5 = workbook.add_worksheet()
    worksheet5.name = 'descriptives'
    worksheet5.write(0, 0, 'descriptive stats')
    for i in range(6):
        worksheet5.write(1, i+1, y[i])
    for i in range(len(x)):
        worksheet5.write(i+2, 0, x[i])
    for i in range(a.shape[1]):
        for j in range(a.shape[0]):
            worksheet5.write(j+2, i+1, str(a[j, i]))
    workbook.close()


def descriptive_stats_RLST(data, LABELmonths3, Lx, f, lst_or_rlst):
    """Compute, display & save to xlsx descriptive statistics for Rdata """
    import matplotlib.pyplot as plt
    from scipy.stats import kurtosis
    from scipy.stats import skew
    print('\nCompute, display & save (to xlsx) descriptive statistics')
    f.write('\n Compute, display descriptive statistics')
    compute_descriptive_stats(data, LABELmonths3, lst_or_rlst)
    x = np.arange(0, len(Lx), 1)
    plt.figure(1)
    plt.xticks(x, Lx)
    plt.title('Absolute skew, kurtosis')
    c = abs(kurtosis(data, axis=0))
    b = abs(skew(data, axis=0))
    plt.plot(c, marker='D', markersize=4, linestyle='-',
             color='r', label='|Kurtosis|')
    plt.plot(b, marker='o', markersize=4, linestyle='--',
             color='b', label='|Skew|')
    plt.legend()
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    if lst_or_rlst == 'RLST':
        plt.savefig('RLST_abs_kurtosis_skew.png', dpi=300)
        f.write('\n    Write Rdata stats to descriptives_RLST.xlsx')
    else:
        plt.savefig('LST_abs_kurtosis_skew.png', dpi=300)
        f.write('\n    Write Rdata stats to descriptives_LST.xlsx')
    plt.show(1)
    plt.close("all")
    f.write('\n    Save absolute kurtosis & skew to abs_kurtosis_skew.png')


def print_RMS(Reconstruct, x, filename2, f):
    """ Write elevation difference stats among DEM pairs to xls file"""
    import xlsxwriter
    print('SAVE DEM comparisons: ', filename2)
    f.write('\n SAVE DEM to DEM comparisons:'+filename2)
    data = dem_differences_stdev(Reconstruct)
    workbook = xlsxwriter.Workbook(filename2)
    worksheet1 = workbook.add_worksheet()
    worksheet1.write(1, 0, 'stdev among differences among 2 DEMs')
    worksheet1.name = 'stdev_of_dif'
    for i in range(0, data.shape[0]):
        worksheet1.write(1, i+2, x[i])
        worksheet1.write(i+2, 1, x[i])
        for j in range(0, data.shape[1]):
            worksheet1.write(i+2, j+2, str(round(data[i, j], 4)))
    data = dem_differences_absoulte_mean(Reconstruct)
    worksheet2 = workbook.add_worksheet()
    worksheet2.write(1, 0, 'mean absolute difference among 2 DEMs')
    worksheet2.name = 'abs_mean_dif'
    for i in range(0, data.shape[0]):
        worksheet2.write(1, i+2, x[i])
        worksheet2.write(i+2, 1, x[i])
        for j in range(0, data.shape[1]):
            worksheet2.write(i+2, j+2, str(round(data[i, j], 4)))
    data = dem_differences_RMS(Reconstruct)
    worksheet3 = workbook.add_worksheet()
    worksheet3.write(1, 0, 'RMSE among 2 DEMs')
    worksheet3.name = 'RMSE'
    for i in range(0, data.shape[0]):
        worksheet3.write(1, i+2, x[i])
        worksheet3.write(i+2, 1, x[i])
        for j in range(0, data.shape[1]):
            worksheet3.write(i+2, j+2, str(round(data[i, j], 4)))
    data = dem_differences_mean(Reconstruct)
    worksheet4 = workbook.add_worksheet()
    worksheet4.write(1, 0, 'Mean among 2 DEMs')
    worksheet4.name = 'Mean_dif'
    for i in range(0, data.shape[0]):
        worksheet4.write(1, i+2, x[i])
        worksheet4.write(i+2, 1, x[i])
        for j in range(0, data.shape[1]):
            worksheet4.write(i+2, j+2, str(round(data[i, j], 4)))
    workbook.close()


def MainRun(data, rows, cols, GeoExtent, FigureLabels, LabelLST, LabelLSTxls,
            Hmin, Hmax):
    """ Main run module of SVR_CLU.py"""
    f, oldpath = findpaths_data2csv(data)
    xyxstr = 'Display statistics of input Data ? '
    Display_yesno2 = input_screen_str_yn(xyxstr)
    if Display_yesno2 == 'Y' or Display_yesno2 == 'y':
        f.write('\n DISPLAY:descriptive stats of input data')
        data2 = data[:, 1:data.shape[1]]
        print_RMS(data2, LabelLSTxls, '_initial_DEMS_DIF_stats.xlsx', f)
        descriptive_stats_RLST(data2, LabelLSTxls, LabelLST, f, 'LST')
    f.close()
    from os import chdir
    chdir(oldpath)
