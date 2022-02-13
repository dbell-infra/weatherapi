from sqlalchemy import create_engine, MetaData, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
import time

import os

Base = declarative_base()


class TemperatureQuery(Base):
    """
    Defines model to store data in DB
    """
    __tablename__ = "queries"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(String)
    query_time = Column(DateTime(timezone=True), server_default=func.now())


# Prep the Postgres Environment and SQLAlchemy config
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
SQLALCHEMY_URL = f"postgresql://weatherapi:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/weatherapi"
engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()

query_table = TemperatureQuery.__table__


def setup_db():
    Base.metadata.create_all(engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()