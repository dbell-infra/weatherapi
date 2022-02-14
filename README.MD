# WeatherAPI
![CI](https://github.com/dm-bell-networking/weatherapi/actions/workflows/python-app.yml/badge.svg)

WeatherAPI is a RESTful API that returns weather data

Weather API uses FastAPI as the API framework and Postgres as the DB for caching weather queries

## Live Demo
Interact with the API here at: http://ec2-18-220-19-215.us-east-2.compute.amazonaws.com/docs
# Local Installation
Before running the setup commands below, ensure you have exported the following environment variables

WEATHER_API_KEY - An API key from the openweather service, sign up for free tier here: https://openweathermap.org/api

POSTGRES_PASSWORD - Your desired postgres password
## Installation via Vagrant
Once vagrant has been installed on your machine run ``vagrant up`` from repository root

## Installation via docker-compose
Once docker and docker-compose have been installed on your machine, run ```docker-compose up -d``` from the repository root.

## Connecting Locally 

WeatherAPI returns data for Portland by default.

if installing via docker-compose, the API will serve requests on port 80
```commandline
curl localhost/temperature
{"query_time":"2022-02-14 02:36:16.980862+00:00","temperature":"54.1"}%   
```

if installing via Vagrant, the API will serve requests on 8080
```commandline
curl http://localhost:8080/temperature
{"query_time":"2022-02-14 02:33:47.551191+00:00","temperature":"54.1"}%   
```

A query string can optionally be used to request cities other than portland
```commandline
curl -X GET "http://localhost/temperature?city=chicago"

{"query_time":"2022-02-14 02:39:32.946563+00:00","temperature":"12.9"}%  
```

Optionally, the FastAPI documentation page can be used to test the API at ```http://locahost:<port>/docs```


# Contributing 
Install the developer requirements with ``pip install -r requirements.dev.txt``

Run ``docker-compose -f docker-compose-dev.yml`` to get a test DB and postgres admin container

Run ```pytest -v``` from the repository root to run the test suite
