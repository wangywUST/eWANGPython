# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:42:25 2018

@author: ywanggp
"""
import numpy as np
from obtainScore import *

def fillPath(loc1, loc2,windGra):
    xPath = np.linspace(loc1[0] + (loc2[0] - loc1[0]) / abs(loc2[0] - loc1[0]), loc2[0], abs(loc2[0] - loc1[0]))
    yPath = np.linspace(loc1[1] + (loc2[1] - loc1[1]) / abs(loc2[1] - loc1[1]), loc2[1], abs(loc2[1] - loc1[1]))
    xPath = np.column_stack((xPath, np.repeat(loc1[1], abs(loc2[0] - loc1[0]))))
    yPath = np.column_stack((np.repeat(loc2[0], abs(loc2[1] - loc1[1])), yPath))
    Path = np.concatenate((xPath, yPath), axis = 0).astype(int)
    score = obtainScore(Path, windGra)
    return(Path,score)