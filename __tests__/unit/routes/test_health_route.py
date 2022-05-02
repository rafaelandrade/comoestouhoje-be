from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_route():
    endpoint = "/health"
    response = client.get(endpoint)

    json_response = response.json()

    assert response.status_code == 200
    assert json_response["message"] == "Hello World!"
