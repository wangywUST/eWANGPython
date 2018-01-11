# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:52:37 2018

@author: ywanggp
"""
from heuristicSquareAlg import *
import numpy as np
from fillPath import *

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
        (newLoc, flag) = heuristicSquareAlg(windGra, lastLoc.copy(), destination, timePieceMin)
        print(i)
        print(lastLoc)
        print(newLoc)
        if(i == 0):
            locList = np.concatenate((np.asarray([locList]), fillPath(lastLoc, newLoc)), axis = 0)
        else:
            locList = np.concatenate((locList, fillPath(lastLoc, newLoc)), axis = 0)
        if(flag == True):
            break
    return(locList)