from fastapi.testclient import TestClient
from weather_api.main import app

client = TestClient(app)


def test_get_temperature_default():
    response = client.get('/temperature')
    assert response.status_code == 200
    for key in ['query_time', 'temperature']:
        assert key in response.json().keys()


def test_get_temperature_city():
    response = client.get('/temperature?city=oakland')
    assert response.status_code == 200
    for key in ['query_time', 'temperature']:
        assert key in response.json().keys()


def test_get_temperature_invalid_city():
    response = client.get('/temperature?city=invalidcityname')
    assert response.status_code == 404
    assert response.json() == {
            "msg": f"could not locate city invalidcityname"
        }