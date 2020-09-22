import pandas as pd


def read_file(path):
    path_root = path
    return pd.read_excel(path_root, sheet_name=0)


def get_column_values(dataframe, column):
    column_values = dataframe[column]
    return list(column_values)
