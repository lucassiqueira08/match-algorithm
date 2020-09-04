from services.similarity import SimilarityService
from services.extrator import read_file, get_column_values


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
