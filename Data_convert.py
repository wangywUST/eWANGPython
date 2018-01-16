# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:17:13 2018

@author: lwuag
"""

def Data_convert(Data, thre_wind):  
    for k in range(Data.shape[0]):
        for i in range(Data.shape[1]):
            for j in range(Data.shape[2]):
                if Date[k, i, j] < thre_wind:
                    Date[k, i, j] = 0 if if Date[k, i, j] < thre_wind else 1
    for k in range(Data.shape[0]-1):
        Date[k,:,:] = Date[k, :, :] or Date[k + 1, :, :]
    return Date