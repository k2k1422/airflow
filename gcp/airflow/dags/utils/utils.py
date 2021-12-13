import pandas as pd
import pytz
import datetime
from sqlalchemy.types import *


def convert_result_to_df(data):
    # print(data,type(data))
    df = pd.DataFrame(data)
    df.columns = data[0].keys()
    return df