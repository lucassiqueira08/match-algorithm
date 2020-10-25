import pandas as pd
import openpyxl

def read_file(path):
    path_root = path
    return pd.read_excel(path_root, sheet_name=0)


def get_column_values(dataframe, column):
    column_values = dataframe[column]
    return list(column_values)

def package_sheet(datas):
    list_data = []
    for data in datas:
        list_temp= data['row_rawdata'], data['row_true'], data['jaccard'], data['similarity'] 
        list_data.append(list_temp)
    sheet = pd.DataFrame(list_data,
                        columns=['row_rawdata', 'row_true', 'jaccard', 'similarity']) 

    return sheet

def export_file(matchs, inconclusive, no_match):
    matchs = package_sheet(matchs)
    inconclusive = package_sheet(inconclusive)
    no_match = package_sheet(no_match)

    with pd.ExcelWriter('export_result.xlsx') as writer:  
        matchs.to_excel(writer, sheet_name='matchs')
        inconclusive.to_excel(writer, sheet_name='inconclusive')
        no_match.to_excel(writer, sheet_name='no_match')
