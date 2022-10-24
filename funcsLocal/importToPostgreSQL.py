
import os
import pandas as pd
import numpy as np

from sqlalchemy import create_engine

from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv() 

def importToPostgreSQL(aggregatedBikesYear,nameTable):
    POSTGRESUSER=os.environ.get('POSTGRESUSER')
    POSTGRESPASSWORD=os.environ.get('POSTGRESPASSWORD')
    POSTGRESHOST=os.environ.get('POSTGRESHOST')
    POSTGRESDB=os.environ.get('POSTGRESDB')
    engine = create_engine(f"postgresql+psycopg2://{POSTGRESUSER}:{POSTGRESPASSWORD}@{POSTGRESHOST}/{POSTGRESDB}")
    aggregatedBikesYear.to_sql(nameTable, engine, if_exists='replace')

    testString=f'SELECT * FROM {nameTable} LIMIT 10'
    resultTest = pd.read_sql_query(testString, engine)
    return resultTest