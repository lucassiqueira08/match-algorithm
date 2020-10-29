from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *
from sqlalchemy import distinct
from sqlalchemy import func


# Create database engine
engine = create_engine('sqlite:///database.db', echo=False)
db_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

Base = declarative_base()
Base.query = db_session.query_property()
Base.metadata.bind = engine 

def init_db():
    Base.metadata.create_all(bind=engine)

def create(objects):
    if type(objects) == list:
        db_session.add_all(objects)
    else:
        db_session.add(objects)
    db_session.commit()
    return objects

def result_filter(object, id_empresa, match):
    select = db_session.query(object).filter(object.company_id == id_empresa, object.matched == match)
    return [result for result in select]



def result_filter_inconclusive(object, id_empresa, inconclusive, related_object):
    result = []
    comparations = db_session.query(object).filter(object.company_id == id_empresa, object.matched == inconclusive).order_by(object.rawdata_id)
    for comparation in comparations:
        group = []
        for comp in comparations:
            if comp.rawdata_id == comparation.rawdata_id:
                new_comp = comp.__dict__
                new_comp['total'] = new_comp['jaccard'] + new_comp['similarity']
                if new_comp not in group:
                    group.append(new_comp)
        
        new_group = sorted(group, key=lambda x: x['total'])
        new_group = new_group[0:4]
        print(len(new_group), new_group[0]['total'], new_group[0]['rawdata_id'], new_group[0]['product_id'])
        result.extend(new_group)

    # select = db_session.query(object).filter(object.company_id == id_empresa, object.matched == inconclusive).distinct(object.rawdata_id.name)
    # select = db_session.query(object).join(related_object, object.rawdata_id==related_object.id).distinct(related_object.description)
    # print(result.all())
    print(f'result ------------------ ${result}')
    return result

def select(object):
    result = db_session.query(object).all()
    return result

def select_filter(object, id):
    select = db_session.query(object).filter(object.id == id)
    return [result for result in select]

def select_filter_rawdata(object, id):
    select = db_session.query(object).filter(object.company_id == id)
    return [result for result in select]
