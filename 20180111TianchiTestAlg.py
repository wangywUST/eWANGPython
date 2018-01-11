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
df1 = pd.read_csv(file, chunksize = chunksize)

for i in range(1, 11):
    if(i == 1):
        pathList = givePath(df, np.asarray([xCity[0], yCity[0]]), 
                            np.asarray([xCity[i], yCity[i]]), 
                            xsize, ysize)
    else:
        pathList = np.concatenate((pathList, givePath(df, np.asarray([xCity[0], yCity[0]]), 
                                                      np.asarray([xCity[i], yCity[i]]), 
                            xsize, ysize)), axis = 0)  

df1_block = df1.get_chunk(chunksize)
windGra = df1_block["wind"].values.reshape(xsize,ysize)
x = np.linspace(1, xsize, xsize)
y = np.linspace(1, ysize, ysize)
X,Y = np.meshgrid(y, x)
CS = plt.contour(X, Y, windGra,levels = [15],
                 colors=('k',),linestyles=('-',),linewidths=(1,))
CSF = plt.contourf(X, Y, windGra, 8, alpha=.95, cmap=plt.cm.cool)
plt.clabel(CS, fmt = '%2.1d', colors = 'k', fontsize=14) #contour line labels
plt.colorbar(CSF, shrink=0.8, extend='both')
plt.scatter(yCity[1:11], xCity[1:11], marker='x', s=50, c = 'gold', zorder=10)
plt.scatter(pathList[:,1], pathList[:, 0], marker='x', s=5, c = 'gold', zorder=10)
plt.scatter(yCity[0], xCity[0], marker='*', s=50, c = 'gold', zorder=10)
plt.show()