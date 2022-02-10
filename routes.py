from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import os
from openweather import get_weather
from schema import TemperatureResponse
from crud import create_temperature_query
from database import get_db
import time

router = APIRouter()

API_KEY = os.getenv('WEATHER_API_KEY')


@router.get("/temperature", response_model=TemperatureResponse)
def get_current_temperature(city: str = "portland", db: Session = Depends(get_db)):
    """
    Gets temperature data based on location as provided by query string and returns JSON

    :param city: Desired city to return data regarding. Default: Portland
    :return: TemperatureResponse Schema
    """
    weather_data = get_weather(API_KEY, city=city)
    if weather_data['status'] != 200:
        return {
            "msg": "The weather service is experiencing trouble"
        }

    response = TemperatureResponse(query_time=time.time(),
                                   temperature=weather_data['data']['list'][0]['main']['temp'])

    create_temperature_query(db, query=response, city=city)



    return response.dict()
