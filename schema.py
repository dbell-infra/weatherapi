from pydantic import BaseModel


class TemperatureResponse(BaseModel):
    query_time: str
    temperature: str
