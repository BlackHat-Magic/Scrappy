from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Image(Base):
    __tablename__ = "Images"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    siteid = Column(String)
    url = Column(String)
    tags = Column(PickleType)
    height = Column(Integer)
    width = Column(Integer)