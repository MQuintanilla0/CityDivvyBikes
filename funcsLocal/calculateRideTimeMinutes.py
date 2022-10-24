import os
import pandas as pd

def calculateRideTimeMinutes(dataBikesDict):
    keyName=""
    for keyName, eachMonthBikes in dataBikesDict.items():
        eachMonthBikes["ride_time"]=pd.to_datetime(eachMonthBikes["ended_at"])-pd.to_datetime(eachMonthBikes["started_at"])
        eachMonthBikes["ride_time_minutes"]=eachMonthBikes["ride_time"].dt.total_seconds() / 60
        print(eachMonthBikes['ride_time_minutes'].sample(frac = 0.2))
        print(eachMonthBikes['ride_time_minutes'].describe())
        print(eachMonthBikes['ride_time_minutes'].info())
    
    return dataBikesDict