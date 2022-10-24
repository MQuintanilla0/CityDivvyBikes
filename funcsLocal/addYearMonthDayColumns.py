import os
import pandas as pd

def addYearMonthDayColumns(dataBikesDict):
    keyName=""
    for keyName, eachMonthBikes in dataBikesDict.items():
        eachMonthBikes['year']= pd.to_datetime(eachMonthBikes['started_at']).dt.year
        eachMonthBikes['month']= pd.to_datetime(eachMonthBikes['started_at']).dt.month
        eachMonthBikes['day']= pd.to_datetime(eachMonthBikes['started_at']).dt.day

        eachMonthBikes["day_of_week"]=pd.to_datetime(eachMonthBikes["started_at"])
        eachMonthBikes["day_of_week"]=eachMonthBikes["day_of_week"].dt.day_name()
        """
        day of week meaning monday, thursday, wednesday... of starting ride
        """
    return dataBikesDict