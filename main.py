# main.py

from extract import download_and_extract
from transform import transform_data
from load import load_to_sql
from config import FILENAME

def run_etl():
    print("Starting ETL process...")
    
    # Extract
    download_and_extract()

    # Transform
    df = transform_data(FILENAME)

    # Load
    load_to_sql(df)

    print("ETL process completed successfully.")

if __name__ == '__main__':
    run_etl()
