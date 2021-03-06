from services.similarity import SimilarityService
from services.extrator import read_file, get_column_values, export_file
from data.models import Company, Product, RawData, Comparation
from data.base import init_db, create, select, select_filter, select_filter_rawdata, result_filter
import time

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

            id = int(input(' Digite o id da empresa : '))
            table_true = select(Product)
            table_rawdata = select_filter_rawdata(RawData, id)
            
            list_no_match = []
            list_ava = []
            list_match = []
            result = []
            for row_data_target in table_rawdata:
                for row_data_true in table_true:
                    comparation = main(row_data_target.description, row_data_true.description)
                    if not comparation == None:
                        comparation['row_rawdata'] = row_data_target.id
                        comparation['row_true'] = row_data_true.id
                        result.append(Comparation(company_id= id, 
                                                  product_id=row_data_true.id,
                                                  rawdata_id=row_data_target.id,
                                                  jaccard= comparation['jaccard'],
                                                  similarity= comparation['similarity'], 
                                                  matched= comparation['matched'],
                                                  ))
            create(result)
            

            # create(Company(name=str(input(" Digite o nome da empresa : "))))

                        # if comparison.get('similarity') > 85.00 or comparison.get('jaccard') > 85.00:
                        #     comparison['row_rawdata'] = row_data_target.description
                        #     comparison['row_true'] = row_data_true.description
                        #     list_match.append(comparison)
                        # elif comparison.get('similarity') >= 65.00 and comparison.get('similarity') <= 84.99 or comparison.get('jaccard') >= 65.00 and comparison.get('jaccard') <= 84.99:
                        #     comparison['row_rawdata'] = row_data_target.description
                        #     comparison['row_true'] = row_data_true.description
                        #     list_ava.append(comparison)
                        # else:
                        #     comparison['row_rawdata'] = row_data_target.description3
                        #     comparison['row_true'] = row_data_true.description
                        #     list_no_match.append(comparison)


                    
            # print("""

            #     * Results *

            #     matchs - {}

            #     Inconclusive - {}

            #     no_matchs - {}
            
            # """.format(len(list_match), len(list_ava), len(list_no_match)))
            
        if option == 4:
            id = int(input(' Digite o id da empresa : '))

            # print(len(result_filter(Comparation, id)))
            inicio = time.time()
            x = []
            list_matchs = []
            list_inconclusive = []
            list_nomatchs = []
            for row in result_filter(Comparation, id):
                if row.matched == 'match':
                    print('')
                x.append(row.__dict__)

            temp_m =[]
            temp_a =[]
            temp_n =[] 
            rawadatas_ids = []

            for i in range(len(x)): 
                now = i

                if x[now]['matched'] == 'match':
                    x[now]['total'] = x[now]['similarity']+ x[now]['jaccard']
                    temp_m.append(x[now])
                
                if x[now]['matched'] == 'inconclusive':
                    x[now]['total'] = x[now]['similarity']+ x[now]['jaccard']
                    temp_a.append(x[now])

                if x[now]['matched'] == 'no_match':
                    x[now]['total'] = x[now]['similarity']+ x[now]['jaccard']
                    temp_n.append(x[now])

            temp_m = sorted(temp_m, key=lambda x: x['total'], reverse=True)
            temp_a = sorted(temp_a, key=lambda x: x['total'], reverse=True)
            temp_n = sorted(temp_n, key=lambda x: x['total'], reverse=True)

            for i in range(len(temp_m)):
                now = i
                prox = i+1
                if prox >= len(temp_m):
                    prox = i
                if not temp_m[now]['rawdata_id'] in rawadatas_ids:
                    temp_list = []
                    for search in temp_m:
                        if search['rawdata_id'] == temp_m[now]['rawdata_id']:
                            temp_list.append(search)    
                    list_matchs.append(temp_list[0])   
                    rawadatas_ids.append(temp_m[now]['rawdata_id'])

            print('')
            print(rawadatas_ids)
            matchs_export = []

            for lists in list_matchs:
                if type(lists) == list:
                    for y in lists:
                        print(y)
                        product = select_filter(Product, y['product_id'])
                        rawdata = select_filter(RawData, y['rawdata_id'])
                        y['product_id'] = product[0].description
                        y['rawdata_id'] = rawdata[0].description
                        matchs_export.append(y)
                else:
                    print(lists)
                    product = select_filter(Product, lists['product_id'])
                    rawdata = select_filter(RawData, lists['rawdata_id'])
                    lists['product_id'] = product[0].description
                    lists['rawdata_id'] = rawdata[0].description
                    matchs_export.append(lists)
                    

            for i in range(len(temp_a)):
                now = i
                prox = i+1
                if prox >= len(temp_a):
                    prox = i

                if not temp_a[now]['rawdata_id'] in rawadatas_ids:
                    temp_list = []
                    for search in temp_a:
                        if search['rawdata_id'] == temp_a[now]['rawdata_id']:
                            temp_list.append(search)
                    list_inconclusive.append(temp_list[0:5])
                    rawadatas_ids.append(temp_a[now]['rawdata_id'])


            print('')
            print(rawadatas_ids)
            inconclusive_export = []
            for lists in list_inconclusive:
                print('')
                for y in lists:
                    print(y)
                    product = select_filter(Product, y['product_id'])
                    rawdata = select_filter(RawData, y['rawdata_id'])
                    y['product_id'] = product[0].description
                    y['rawdata_id'] = rawdata[0].description
                    inconclusive_export.append(y)

            for i in range(len(temp_n)):
                now = i
                prox = i+1
                if prox >= len(temp_n):
                    prox = i
                if not temp_n[now]['rawdata_id'] in rawadatas_ids:
                    temp_list = []
                    for search in temp_n:
                        if search['rawdata_id'] == temp_n[now]['rawdata_id']:
                            temp_list.append(search)
                    list_nomatchs.append(temp_list[0:5])
                    rawadatas_ids.append(temp_n[now]['rawdata_id'])

            print('')
            print(rawadatas_ids)
            nomatch_export = []
            for lists in list_nomatchs:
                print('')
                for y in lists:
                    print(y)
                    product = select_filter(Product, y['product_id'])
                    rawdata = select_filter(RawData, y['rawdata_id'])
                    y['product_id'] = product[0].description
                    y['rawdata_id'] = rawdata[0].description
                    nomatch_export.append(y)
                    

            export_file(matchs_export, inconclusive_export, nomatch_export)

            fim = time.time()

            print('')
            print(""" Tempo de execução .: {}""".format((fim - inicio)))

        
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
            print(result[0].name)


