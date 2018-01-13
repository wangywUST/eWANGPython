# -*- coding: utf-8 -*-

def jumpDays(df, numDay, chunksize):
    for i in range(1, numDay):
        for j in range(18):
            df.get_chunk(chunksize)
            
    return df
    