# -*- coding: utf-8 -*-

def obtainScore(pathList, windGra):
    timeLen = pathList.shape[0]
    threshold = 15
    for i in range(timeLen):
        if(windGra[pathList[i, 0], pathList[i, 1]] >= threshold):
            return 1440
    return((timeLen - 1) * 2)