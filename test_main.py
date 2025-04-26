from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_client_info():
    response = client.post("/client-info")
    assert response.status_code == 200
    data = response.json()
    assert "user_agent" in data
    assert "ip" in data
    assert "forwarded_for" in data
    assert "real_ip" in data 