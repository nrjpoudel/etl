# extract.py

import kaggle
import zipfile
import os
from config import DATASET, FILENAME, ZIPFILE

def download_and_extract():
    # Download the dataset
    os.system(f'kaggle datasets download {DATASET} -f {FILENAME}')
    
    # Extract the dataset
    with zipfile.ZipFile(ZIPFILE, 'r') as zip_ref:
        zip_ref.extractall()
    print(f"{FILENAME} extracted successfully.")

if __name__ == '__main__':
    download_and_extract()
