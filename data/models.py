from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from .base import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    long_description = Column(String)

    def __init__(self, long_description,*args, **kwargs):
        self.long_description = long_description

class RawData(Base):
    __tablename__ = 'rawdatas'
    id = Column(Integer, primary_key=True)
    description = Column(String)   

    def __init__(self, description,*args, **kwargs):
        self.description = description
    
class Comparation(Base):
    __tablename__ = 'comparations'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    rawdata_id = Column(Integer, ForeignKey('rawdatas.id'))
    distance = Column(Float)
    similarity = Column(Float)
    jaccard = Column(Float)
    matched = Column(Boolean)

    def __init__(self, product_id,rawdata_id,distance,similarity,jaccard,matched,*args, **kwargs):
        self.product_id = product_id
        self.rawdata_id = rawdata_id
        self.distance = distance
        self.similarity = similarity
        self.jaccard = jaccard
        self.matched = matched