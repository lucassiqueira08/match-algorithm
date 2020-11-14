from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from .base import Base


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String) 

    def __init__(self, name, *args, **kwargs):
        self.name = name

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __init__(self, description, *args, **kwargs):
        self.description = description

class RawData(Base):
    __tablename__ = 'rawdata'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    description = Column(String)   

    def __init__(self, company_id, description, *args, **kwargs):
        self.description = description
        self.company_id = company_id
    
class Comparation(Base):
    __tablename__ = 'comparations'
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    rawdata_id = Column(Integer, ForeignKey('rawdata.id'))
    similarity = Column(Float)
    jaccard = Column(Float)
    matched = Column(String)

    def __init__(self, company_id, product_id, rawdata_id, similarity, jaccard, matched, *args, **kwargs):
        self.company_id = company_id
        self.product_id = product_id
        self.rawdata_id = rawdata_id
        self.similarity = similarity
        self.jaccard = jaccard
        self.matched = matched
