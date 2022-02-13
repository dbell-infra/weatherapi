from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import os
from openweather import get_weather
from schema import TemperatureResponse
from crud import create_temperature_query, get_temperature_query
from database import get_db
from helpers import compare_timestamps
from datetime import datetime, timezone

router = APIRouter()

API_KEY = os.getenv('WEATHER_API_KEY')


@router.get("/temperature", response_model=TemperatureResponse)
def get_current_temperature(city: str = "portland", db: Session = Depends(get_db)):
    """
    Gets temperature data based on location as provided by query string and returns JSON

    :param city: Desired city to return data regarding. Default: Portland
    :param db: Database dependency injection
    :return: TemperatureResponse Schema
    """
    # Get time of query
    query_time = datetime.now(timezone.utc)

    # Check for existing query
    db_query = get_temperature_query(db, city=city)

    # If query exists and time comparison returns true, serve query from DB
    if db_query and compare_timestamps(db_time=db_query.query_time, query_time=query_time):
        print(f"INFO: Found record in cache DB for city: {city} time: {query_time} that satisfies cache requirements ")
        response = TemperatureResponse(query_time=str(query_time), temperature=db_query.temperature)
        return response.dict()



    # If the above conditions do not result in the function returning, either a query does not exist, or the cache data
    # is stale, proceed to get weather data via data provider.
    print(f"INFO: Unable to find satisfactory cache data for query city: {city}, time: {query_time}")
    weather_data = get_weather(API_KEY, city=city)

    # If we do not have a successful call to provider return error message
    if weather_data['status'] != 200:
        return {
            "msg": "The weather service is experiencing trouble"
        }

    # If city name is invalid, return message to the client
    if not weather_data['validity']:
        return {
            "msg": f"could not locate city {city}"
        }

    # Send response to the user and cache query in DB
    response = TemperatureResponse(query_time=str(query_time),
                                   temperature=weather_data['data']['list'][0]['main']['temp'])
    print(f"INFO: Creating entry in cache DB for city: {city} time: {query_time} ")
    create_temperature_query(db, query=response, city=city)

    return response.dict()
