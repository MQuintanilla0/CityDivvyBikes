import pandas as pd
import numpy as np
import os

def concatenateAllBikeData(dataBikesDict):
    aggregatedBikesYear=pd.DataFrame(columns=dataBikesDict['202110'].columns)
    for keyName, eachMonthBikes in dataBikesDict.items():
        aggregatedBikesYear = pd.concat([aggregatedBikesYear,eachMonthBikes],ignore_index=True)
    return aggregatedBikesYear