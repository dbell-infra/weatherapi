import requests
import os




def get_weather(api_key: str, city: str="portland") -> dict:
    """
    Makes call to external weather service and returns weather data

    :param api_key: OpenWeatherMap API Key
    :param city: City to return data for
    :return: dictionary containing status code and data if call was successful
    """
    url = f"https://api.openweathermap.org/data/2.5/find?q={city}&units=imperial&appid={api_key}&limit=1"
    response = requests.get(url)
    if response.status_code != 200:
        return {
            "status": response.status_code
        }
    return {
        "status": response.status_code,
        "data":  response.json()
    }