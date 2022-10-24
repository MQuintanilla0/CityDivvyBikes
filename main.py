import os
import pandas as pd
import numpy as np
from funcsLocal.funcList import *
import matplotlib
from dotenv import load_dotenv
from sqlalchemy import create_engine

"""
TO BE ADDED
"""
#import seaborn as sns
#import dash
#import plotly.express as px



"""
Get current working directory
"""

currentDirectory = os.getcwd()

"""
Add to the path the folder that will have the data
"""
newPathtoRead = currentDirectory +"/DataSource/" 

"""
Get the folders with listdir on the source data folder
"""
DataFolderList = os.listdir(newPathtoRead)

dataBikesDict = {}

"""
Cycle through the folders according to every month from 2021-10 to 2022-09
Then check if there is a file inside a folder that ends with .csv to read and store it on
dataBikesDict as a dataframe with the yearmonth as the keyName
"""

dataBikesDict = readCSVfromFolders(DataFolderList,newPathtoRead)


"""
Function prints summarized data
"""

dataBikesDict = calculateRideTimeMinutes(dataBikesDict)
dataBikesDict = addYearMonthDayColumns(dataBikesDict)

"""
Calculate ride time on each cyclist on each month and add Year Month Day columns
"""

pivotMembersAverageRideLength = pivotMembersAverageRideLength(dataBikesDict)
pivotMembersAverageRideLengthByDayStart = pivotMembersAverageRideLengthByDayStart(dataBikesDict)
pivotMembersNumberOfRides = pivotMembersNumberOfRides(dataBikesDict)

"""
Pivot tables for analysis
"""

aggregatedBikesYear = concatenateAllBikeData(dataBikesDict)

"""
Aggregate all data in only one dataframe for csv creation

"""

aggregatedBikesYear2021 = separateDataByYear(aggregatedBikesYear,2021)
aggregatedBikesYear2022 = separateDataByYear(aggregatedBikesYear,2022)

"""
Separate data in 2021 and 2022 because Tableau only supports 1 gb files, could use chunksize= in other cases
"""
aggregatedBikesYear2021.to_csv('aggregatedBikesYear2021.csv',index=False)
aggregatedBikesYear2022.to_csv('aggregatedBikesYear2022.csv',index=False)
"""
Export to CSV for Tableau
"""

checkString = importToPostgreSQL(aggregatedBikesYear,'aggregatedbikesyear')

print(checkString)
"""
Export to SQL for PowerBI
"""
print("done")
