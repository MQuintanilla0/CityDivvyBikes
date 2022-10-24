import pandas as pd
import numpy as np
import os

def pivotMembersAverageRideLengthByDayStart(dataBikesDict):
    pivotMembersAverageRideLengthByDayStart={}
    for keyName, eachMonthBikes in dataBikesDict.items():
        pivotMembersAverageRideLengthByDayStart[keyName]=pd.pivot_table(eachMonthBikes,values=['ride_time_minutes'],index=['member_casual'],columns=['day_of_week'],aggfunc=np.mean)
    return pivotMembersAverageRideLengthByDayStart