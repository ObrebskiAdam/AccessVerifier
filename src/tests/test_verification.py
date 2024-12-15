from fastapi.testclient import TestClient
from src.access_verifier.main import app

client = TestClient(app)

def test_verification_without_header():
    response = client.post("/api/v1/verification")
    assert response.status_code == 400

def test_verification_with_unvalid_ip():
    response = client.post("/api/v1/verification", headers={"X-Forwarded-For": "127.0.0.1"})
    assert response.status_code == 401 and response.json()["detail"] == "Ip address is not allowed"

def test_verification_with_valid_ip():
    response = client.post("/api/v1/verification", headers={"X-Forwarded-For": "192.168.1.2"})
    assert response.status_code == 200