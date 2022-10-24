import pandas as pd
import numpy as np
import os

def pivotMembersNumberOfRides(dataBikesDict):
    pivotMembersNumberOfRides={}
    keyName=""
    for keyName, eachMonthBikes in dataBikesDict.items():
        pivotMembersNumberOfRides[keyName]=pd.pivot_table(eachMonthBikes,values=['ride_id'],index=['member_casual'],columns=['day_of_week'],aggfunc=len)
    return pivotMembersNumberOfRides