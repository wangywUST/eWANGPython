# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 17:43:42 2018

@author: lwuag
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 14:25:24 2018

@author: lwuag
"""
import numpy as np
from dijkstar import Graph, find_path


#    star_point = Start_city[0] * col_num + Start_city[1]
#    end_point = Target_city[0] * col_num + Target_city[1]

def Path_design(Data, star_point, end_point, height):
    high_num = int(Data.shape[0])
    row_num = int(Data.shape[1])
    col_num = int(Data.shape[2])
    thre_wind = 15
    graph = Graph()
    for i in range(row_num):
        for j in range(col_num):
            index = i * col_num + j
#            graph.add_node(index)
            if i - 1 >= 0 and Data[height,i - 1, j] < thre_wind:
                index_next = (i - 1) * col_num + j
                graph.add_edge(index, index_next, edge = 2)
            if i + 1 < row_num and Data[height, i + 1, j] < thre_wind:
                index_next = (i + 1) * col_num + j
                graph.add_edge(index, index_next, edge = 2)
            if j - 1 >= 0 and Data[height, i, j - 1] < thre_wind:
                index_next = i * col_num + (j - 1)
                graph.add_edge(index, index_next, edge = 2)
            if j + 1 < col_num and Data[height, i, j + 1] < thre_wind:
                index_next = i * col_num + (j + 1)
                graph.add_edge(index, index_next, edge = 2)
    cost_func = None
    heuristic_func = None
    PathInfo = find_path(graph, star_point, end_point, cost_func, heuristic_func)
    Stop = False
    Fail_pos = 0
    if height == high_num - 1:
        return PathInfo
    else:
        while index in range(30, len(PathInfo)) and not Stop:
            x_id = PathInfo[index] // col_num
            y_id = PathInfo[index] % col_num
            if Data[height, x_id, y_id] >= thre_wind:
                Stop = True
                Fail_pos = index
        if Stop:
            height_start = Fail_pos // 30
            return PathInfo[0:height_start*30] + Path_design(Data, PathInfo[height_start*30], end_point, height_start)
        else:
            return PathInfo
        