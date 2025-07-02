# load.py

import sqlalchemy as sal
from dotenv import load_dotenv
import os
load_dotenv()

SERVER = os.getenv('HOST')
DATABASE = os.getenv('DATABASE')
DRIVER = 'ODBC Driver 17 for SQL Server'
TABLE_NAME = 'df_orders'

def load_to_sql(df):
    connection_string = f"mssql+pyodbc://{SERVER}/{DATABASE}?driver={DRIVER.replace(' ', '+')}"
    engine = sal.create_engine(connection_string)
    conn = engine.connect()

    df.to_sql(TABLE_NAME, con=conn, index=False, if_exists='replace')
    print(f"Data loaded successfully into table '{TABLE_NAME}'.")
