import pandas as pd
import pytz
import datetime
from sqlalchemy.types import *


def convert_result_to_df(data):

    df = pd.DataFrame(data)
    df.columns = data[0].keys()
    return df

def convert_to_utc(epoch_date):

    tz = pytz.timezone("Asia/Kolkata")
    dt = datetime.datetime.fromtimestamp(epoch_date, tz)
    dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    utc_dt = dt.astimezone(pytz.utc)

    return utc_dt

def set_target_dtype(target_col_details_df):

    dtype = {}
    for index, row in target_col_details_df.iterrows(): 
        if "INTEGER" in row['target_column_type']:
            dtype[row['target_column']] = Integer()
        elif "TEXT" in row['target_column_type'] or "VARCHAR" in row['target_column_type']:
            dtype[row['target_column']] = String()
        elif "DECIMAL" in row['target_column_type']:
            dtype[row['target_column']] = Numeric()
        elif "BOOLEAN" in row['target_column_type']:
            dtype[row['target_column']] = Boolean()
        elif "BIGINT" in row['target_column_type']:
            dtype[row['target_column']] = BigInteger()
        elif "TIMESTAMP" in row['target_column_type']:
            dtype[row['target_column']] = DateTime()
    return dtype