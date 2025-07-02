# transform.py
import pandas as pd


def transform_data(csv_file):
    df = pd.read_csv(csv_file)

    # Clean column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Derive new columns
    df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
    df['sale_price'] = df['list_price'] - df['discount']
    df['profit'] = df['sale_price'] - df['cost_price']

    # Convert date
    df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')

    # Drop unnecessary columns
    df.drop(columns=['list_price', 'cost_price', 'discount_percent'], inplace=True)

    return df
