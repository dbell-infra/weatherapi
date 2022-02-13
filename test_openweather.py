from .openweather import get_weather
import os


def test_get_weather_valid_city():
    API_KEY = os.getenv('WEATHER_API_KEY')
    response = get_weather(api_key=API_KEY, city="portland")
    assert response['status'] == 200
    assert response['validity']
    assert "list" in response['data'].keys()
    assert isinstance(response['data']['list'][0], dict)
    assert "temp" in response['data']['list'][0]['main'].keys()


def test_get_weather_invalid_city():
    API_KEY = os.getenv('WEATHER_API_KEY')
    response = get_weather(api_key=API_KEY, city="invalidcityname")
    assert response['status'] == 200
    assert not response['validity']


def test_get_weather_invalid_key():
    API_KEY = "invalidkey"
    response = get_weather(api_key=API_KEY, city="portland")
    assert response['status'] == 401

