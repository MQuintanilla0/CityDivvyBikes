import os
import pandas as pd

def readCSVfromFolders(DataFolderList,newPathtoRead):
    dataBikesDict = {}
    keyName = ""
    for dataFolder in DataFolderList:
        for csvInFolder in os.listdir(newPathtoRead+dataFolder):
            print(csvInFolder)
            if str(csvInFolder).endswith(".csv"):
                keyName = str(csvInFolder)[:6]
                print(keyName)
                dataBikesDict[keyName] = pd.read_csv(newPathtoRead+dataFolder+"/"+csvInFolder)
                print(dataBikesDict[keyName].sample(frac = 0.2))
                print(dataBikesDict[keyName].describe())
                print(dataBikesDict[keyName].info())
    return dataBikesDict