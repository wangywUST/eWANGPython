# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:21:22 2018

@author: ywanggp
"""

import sys
sys.path.append("Functions")
from givePath import *
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np


trainPredFile = "C:/Users/ywanggp/Downloads/ForecastDataforTraining_201712.csv"
trainTrueFile = "C:/Users/ywanggp/Downloads/In_situMeasurementforTraining_201712.csv"
testPredFile = "C:/Users/ywanggp/Downloads/ForecastDataforTesting_201712.csv"
cityLocFile = "C:/Users/ywanggp/Downloads/CityData.csv"

cityLoc = pd.read_csv(cityLocFile)
xCity = cityLoc['xid']
yCity = cityLoc['yid']
file = trainTrueFile

xsize = 548
ysize = 421

chunksize = xsize * ysize
df = pd.read_csv(file, chunksize = chunksize)

pathList = givePath(df, np.asarray([xCity[0], yCity[0]]), np.asarray([xCity[1], yCity[1]]), 
                    xsize, ysize)
