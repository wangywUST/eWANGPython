# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:52:37 2018

@author: ywanggp
"""
from heuristicSquareAlg import *
import numpy as np

def givePath(df, Departure, destination, xsize, ysize):
    chunksize = xsize * ysize
    iniLoc = Departure.copy()
    newLoc = iniLoc.copy()
    hourNum = 18
    timePieceMin = 60
    locList = newLoc 
    for i in range(hourNum):
        lastLoc = newLoc.copy()
        df_block = df.get_chunk(chunksize)
        windGra = df_block["wind"].values.reshape(xsize,ysize)
        (newLoc, flag) = heuristicSquareAlg(windGra, lastLoc, destination, timePieceMin)
        if(i > 0):
            locList = np.concatenate((locList, np.asarray([newLoc])), axis = 0)
        else:
            locList = np.row_stack((locList, newLoc))   
        if(flag == True):
            break
    return(locList)