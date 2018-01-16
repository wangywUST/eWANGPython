# -*- coding: utf-8 -*-
#import matplotlib.pyplot as plt

def obtainScore(pathList, windGra):
    timeLen = pathList.shape[0]
    threshold = 15
    for i in range(timeLen):
        if(windGra[pathList[i, 0], pathList[i, 1]] >= threshold):
#            print "die " + str(windGra[pathList[i, 0], pathList[i, 1]])
#            plt.scatter(pathList[i, 1], pathList[i, 0], marker='+', s=100, c = 'gold', zorder=10), 
            return 1440
    return((timeLen - 1) * 2)