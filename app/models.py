# create models here..
from .database import Base
from sqlalchemy import Column, Integer, String

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)