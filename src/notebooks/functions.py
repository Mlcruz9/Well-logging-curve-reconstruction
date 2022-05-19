import pandas as pd
import numpy as np


def col_to_float(df_column):
    """Returns a column of a pandas DataFrame with its values as float if it`s composed of numbers and contains characters
        like ('.'/','/' ')"""

    df_column = pd.Series([x.replace(".","") for x in df_column])
    df_column = pd.Series([x.replace("-","") for x in df_column])
    df_column = pd.Series([x.replace(" ","") for x in df_column]).astype(float)

    return df_column

def nan_as_nan(df_column_to_edit, nan_value):
    """Returns null float values (ex:999) to null values (None)"""
    df_column_to_edit = np.where(df_column_to_edit == nan_value, None, df_column_to_edit)

    return df_column_to_edit