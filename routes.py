from fastapi import APIRouter
import os
from openweather import get_weather
from schema import TemperatureResponse
import time

router = APIRouter()

API_KEY = os.getenv('WEATHER_API_KEY')


@router.get("/temperature", response_model=TemperatureResponse)
def get_current_temperature(city: str = "portland"):
    """
    Gets temperature data based on location as provided by query string and returns JSON

    :param city: Desired city to return data regarding. Default: Portland
    :return: TemperatureResponse Schema
    """
    weather_data = get_weather(API_KEY, city=city)
    if weather_data['status'] != 200:
        return {
            "msg": "The weather "
        }
    response = TemperatureResponse(query_time=time.time(),
                                   temperature=weather_data['data']['list'][0]['main']['temp'])
    return response.dict()
