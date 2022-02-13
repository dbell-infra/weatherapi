from sqlalchemy.orm import Session

from .schema import TemperatureResponse
from .database import TemperatureQuery


def create_temperature_query(db: Session, query: TemperatureResponse, city: str):
    db_query = TemperatureQuery(
        city=city,
        temperature=query.temperature
    )
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_temperature_query(db: Session, city: str):
    query = db.query(TemperatureQuery).where(TemperatureQuery.city == city).order_by(TemperatureQuery.id.desc()).first()
    return query
