# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 12:21:54 2017

@author: thom
"""
###### IMPORT EXCEL MODULE ######
from xlrd import open_workbook
import numpy as np


def data_importer():
    ###### OPENING THE FILE ######
    wb = open_workbook('formatteddata.xls')


    for sheet in wb.sheets():
        nr = sheet.nrows            #number of rows
        nc = sheet.ncols            #number of columns

        ###### DEFINE WHERE THE DIFFERENT DATA IS ######

        h = [0,12,22,32,42,47]          #position of data, height location
        w = [0,3,10,10,13,13]           #position of data, amount of columns

        ###### ARRAYS CONTAINING DIFFERENT DATA ######

        totallist = [[None],[None],[None],[None],[None]]
        for i in range(1,6):
            values = [[0 for x in range(w[0],w[i])] for y in range(h[i-1],h[i])]
            for col in range(w[0],w[i]):                                            #loop for the amount of columns in the dataset
                for row in range(h[i-1],h[i]):                                      #loop for the amount of rows in the dataset
                    value0  = (sheet.cell(row,col).value)

                    try:
                        value1 = float(value0)                                      #if it is a number, make it a float
                    except ValueError:                                              #if not, keep it as text
                        value1 = value0
                    finally:
                        values[row-h[i-1]][col] = value1                            #put it into the subarray
            totallist[i-1]  = values
            # use a loop to the the fuel flows
            #to get the FFl use totallist[1][i][6] with 3 < i < 9
            #to get the FFr use totallist[1][i][7] with 3 < i < 9

    h_stat1 = []
    h_stat2 = []
    for i in range(3, 10):
        h_stat1.append(totallist[1][i][3])
        h_stat2.append(totallist[3][i][3])

    h_cg_shift = []
    Ffl_cg_shift = []
    Ffr_cg_shift = []
    Temp_cg_shift = []
    for i in range(3, 5):
        h_cg_shift.append(totallist[4][i][3])
        Ffl_cg_shift.append(totallist[4][i][9])
        Ffr_cg_shift.append(totallist[4][i][10])
        Temp_cg_shift.append(totallist[4][i][12])

    return h_stat1, h_stat2, h_cg_shift

# print data_importer()
