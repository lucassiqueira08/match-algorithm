from services.similarity import SimilarityService
from services.extrator import read_file, get_column_values, export_file
from data.models import Company, Product, RawData, Comparation
from data.base import init_db, create, select, select_filter, select_filter_rawdata


def main(reference, target):
    similarity_service = SimilarityService()
    if reference and target:
        return similarity_service.calculate(reference.lower(), target.lower())


def extrator(path, column):
    file = read_file(path)
    values = get_column_values(file, column)
    return values


if __name__ == "__main__":
    init_db()
    close = True

    while close:
        option = int(input("""
            
            1 - Cradastrar Empresa
            
            2 - Subir Base não sanitizada
            3 - Processar Base
            4 - Verificar Resultados.

            7 - Subir tabela verdade
            8 - Print tabela verdade

            9 - Exit
            
        """))

        if option == 1:
            create(Company(name=str(input(" Digite o nome da empresa : "))))
        
        if option == 2:
            id = int(input(' Digite o id da empresa : '))
            rawdata = []
            result = select_filter(Company, id)
            if result != []:
                table_target = str(input('digite o nome do arquivo com a extensão, ex. base_target.xlsx = '))
                column_target = str(input('digite o nome da coluna onde existe a descrição = '))
                table = extrator(table_target, column_target) 
                for row in table:
                    rawdata.append(RawData(company_id=result[0].id, description=row))
                create(rawdata)    
            else:
                print('não existe cliente')

        
        if option == 3:
            count = 0
            id = int(input(' Digite o id da empresa : '))
            table_true = select(Product)
            table_rawdata = select_filter_rawdata(RawData, id)
            list_x = []

            list_no_match = []
            list_ava = []
            list_match = []
            for row_rawdata in table_rawdata:
                count = count + 1
                count_match = 0
                # print("{}---------------------------------".format(count))
                for row_true in table_true:
                    x = main(row_rawdata.description, row_true.description)
                    if not x == None:
                        if x.get('similarity') > 85.00 or x.get('jaccard') > 85.00:
                            x['row_rawdata'] = row_rawdata.description
                            x['row_true'] = row_true.description
                            list_match.append(x)
                        elif x.get('similarity') >= 65.00 and x.get('similarity') <= 84.99 or x.get('jaccard') >= 65.00 and x.get('jaccard') <= 84.99:
                            x['row_rawdata'] = row_rawdata.description
                            x['row_true'] = row_true.description
                            list_ava.append(x)
                            count_match = count_match + 1
                        else:
                            x['row_rawdata'] = row_rawdata.description
                            x['row_true'] = row_true.description
                            list_no_match.append(x)
            # export_file(list_match, list_ava, list_no_match)
            print("""

                * Resultados *

                matchs - {}

                Inconclusive - {}

                no_matchs - {}
            
            """.format(len(list_match), len(list_ava), len(list_no_match)))
        if option == 4:
            print('flwsss')
        
        if option == 7:
            """ subir tabela verdade """
            table = extrator('base_true_full.xlsx', 'DESCRICAO')
            for row in table:
                create(Product(description=row))
            print('ok')    

        if option == 8:
            """ verificar tabela de produtos """
            for row in select(Product):
                print(row.id, row.description)

        if option == 9:
            close = False
            print('hasta la vista baby...')

        if option == 11:
            # companies = select(Company)
            # print([("id - {}, {}".format(company.id, company.name)) for company in companies])
            result = select_filter(Company, 1)
            print(result)




# print

# criar time de execuçao no processamento dos dados
