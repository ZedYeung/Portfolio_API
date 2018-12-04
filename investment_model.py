from sqlalchemy import Column
from sqlalchemy import Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Investment(Base):
    __tablename__ = 'investments'

    id = Column(Integer, primary_key=True)
    company = Column(String(80))
    quantity = Column(Integer)
    cost = Column(Float)
    # creation_date = Column(Date)
    creation_date = Column(String(20))
