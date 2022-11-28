import sys
from fastapi.testclient import TestClient
sys.path.append('../app/')
sys.path.append('../')
from main import app
from app.core.config import settings

client = TestClient(app)

def test_read_item():
    response = client.post("/login/access-token",
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                           data={"username": settings.FIRST_SUPERUSER,
                                 "password": settings.FIRST_SUPERUSER_PASSWORD},
    )
    assert response.status_code == 200
    return response.json()

if __name__ == "__main__":
    test_read_item()


