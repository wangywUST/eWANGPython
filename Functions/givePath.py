# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 15:52:37 2018

@author: ywanggp
"""
from heuristicSquareAlg import *
from showPoint import *
import numpy as np
from fillPath import *

def givePath(df, Departure, destination, xsize, ysize, xCity, yCity):
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
        print(windGra[newLoc[0], newLoc[1]])
        if(i == 0):
            locList = np.concatenate((np.asarray([locList]), fillPath(lastLoc, newLoc)), axis = 0)
        else:
            locList = np.concatenate((locList, fillPath(lastLoc, newLoc)), axis = 0)
        showPoint(windGra, xCity, yCity, locList)
        if(flag == True):
            break
    return((locList.astype(int), windGra))