import sys

sys.path.append("../..")
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, func
from database import Base


class Address(Base):
    __tablename__ = "address"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    unit = Column(String)
    number = Column(String)
    street = Column(Integer)
    city = Column(String)
    district = Column(String)
    region = Column(String)
    postcode = Column(DateTime)
    hash = Column(String, unique=True, index=True)
    type = Column(Boolean)
    coordinates = Column(String)
