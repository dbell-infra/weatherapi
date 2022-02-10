from sqlalchemy.orm import Session, sessionmaker

from schema import TemperatureResponse
from database import TemperatureQuery


def create_temperature_query(db: Session, query: TemperatureResponse, city: str):
    db_query = TemperatureQuery(
        city=city,
        temperature=query.temperature
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query
