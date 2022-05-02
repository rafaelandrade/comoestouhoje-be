from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_route():
    """
    Test related with health check route

    Objective:
     - Should return 200 in case of everything fine with service
    """
    endpoint = "/health"
    response = client.get(endpoint)

    json_response = response.json()

    assert response.status_code == 200
    assert json_response["message"] == "Hello World!"
