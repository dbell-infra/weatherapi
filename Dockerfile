FROM python:3.10
COPY weather_api ./weather_api
RUN pip install -r weather_api/requirements.txt

WORKDIR ./

EXPOSE 80/tcp


CMD ["uvicorn", "weather_api.main:app" , "--host", "0.0.0.0", "--port", "80" ]