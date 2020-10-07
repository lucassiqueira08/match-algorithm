from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *
# Create database engine
engine = create_engine('sqlite:///database.db', echo=True)
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

def select(object):
    result = db_session.query(object).all()
    return result