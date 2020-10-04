from services.similarity import SimilarityService
from services.extrator import read_file, get_column_values
from data.db import db_create_table, db_insert, db_update, db_delete, db_select_all


def main(reference, target):
    similarity_service = SimilarityService()
    return similarity_service.calculate(reference.lower(), target.lower())


def extrator(path, column):
    file = read_file(path)
    values = get_column_values(file, column)
    print(values)


if __name__ == "__main__":
    #    result = main('CAneta azul', 'azul caneta')
    #    print(result)
    extrator('Extracao_banco.xlsx', 'DESCRICAO_LONGA')

    # db_create_table('database','true_table')
    # db_insert('true_table', 'desc_long', 'abraçadeira')
    # db_update('true_table', 'desc_long', 'porca', 1)
    # print(db_select_all('database','true_table'))