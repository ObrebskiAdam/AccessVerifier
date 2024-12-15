from fastapi.testclient import TestClient
from src.access_verifier.main import app
client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200