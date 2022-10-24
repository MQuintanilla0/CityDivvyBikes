import pandas as pd
import numpy as np
import os

def pivotMembersAverageRideLength(dataBikesDict):
    pivotMembersAverageRideLength={}
    keyName=""
    for keyName, eachMonthBikes in dataBikesDict.items():
        pivotMembersAverageRideLength[keyName]=pd.pivot_table(eachMonthBikes,values=['ride_time_minutes'],index=['member_casual'],columns=['start_station_name'],aggfunc=np.mean)
    return pivotMembersAverageRideLength