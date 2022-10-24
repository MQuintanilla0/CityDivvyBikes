import pandas as pd
import numpy as np
import os

def separateDataByYear(aggregatedBikesYear,yearData):

    aggregatedBikesByYear = aggregatedBikesYear[aggregatedBikesYear.year == yearData]
    aggregatedBikesByYear.drop(columns=['year'])
    return aggregatedBikesByYear
