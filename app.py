from services.similarity import SimilarityService
from services.extrator import read_file, get_column_values
from data.models import Product, RawData, Comparation
from data.base import init_db, create, select

def main(reference, target):
    similarity_service = SimilarityService()
    return similarity_service.calculate(reference.lower(), target.lower())


def extrator(path, column):
    file = read_file(path)
    values = get_column_values(file, column)
    print(values)


if __name__ == "__main__":
    init_db()
    #    result = main('CAneta azul', 'azul caneta')
    #    print(result)
    # extrator('Extracao_banco.xlsx', 'DESCRICAO_LONGA')

    # db_create_table('database','true_table')
    # db_insert('child', 'name', 'cesar')
    # db_update('true_table', 'desc_long', 'porca', 1)

    # p1 = Product(long_description='Abraçadeira')
    # p2 = Product(long_description='Abraçadeira Aço')
    # p3 = Product(long_description='Abraçadeira aluminio')

    # r1 = RawData(description='Abraçadeira aluminio')
    # r2 = RawData(description='Abraçadeira aluminio') 
    # r3 = RawData(description='Abraçadeira aluminio') 
    
    # products = [p1, p2, p3]
    # rawdatas = [r1, r2, r3] 

    # create(products)
    # create(rawdatas)

    # c1 = Comparation(product_id=1, rawdata_id=1, distance=50.0, similarity=50.0, jaccard=50.0, matched=True)
    # c2 = Comparation(product_id=2, rawdata_id=2, distance=60.0, similarity=60.0, jaccard=60.0, matched=False)
    # c3 = Comparation(product_id=3, rawdata_id=3, distance=70.0, similarity=70.0, jaccard=70.0, matched=True)

    # comparations = [c1, c2, c3]
    # create(comparations)

    # results = select(Product)

    # for raw in select(RawData):
    #     print(raw.id, raw.description)
    
    # for product in select(Product):
    #     print(product.id, product.long_description)

    for comparation in select(Comparation):
        print(comparation.product_id)    
    
    print("ok")
