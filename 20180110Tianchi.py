import sys
sys.path.append("Functions")
from heuristicSquareAlg import *
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
pd.set_option('display.max_rows', None)
#print(df.get_chunk(chunksize))
for i in range(1):
    df_block = df.get_chunk(chunksize)
    windGra = df_block["wind"].values.reshape(xsize,ysize)
    print(heuristicSquareAlg(windGra, np.asarray([xCity[0], yCity[0]]), np.asarray([xCity[1], yCity[1]]), 60))