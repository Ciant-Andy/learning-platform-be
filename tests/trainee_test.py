import pytest
import sys
from fastapi.testclient import TestClient
sys.path.append('../app/')
sys.path.append('../')
from main import app
from app.core.config import settings

client = TestClient(app)


def test_get_token():
    response = client.post("/login/access-token",
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                           data={"username": settings.FIRST_SUPERUSER,
                                 "password": settings.FIRST_SUPERUSER_PASSWORD},
    )
    assert response.status_code == 200


def get_token():
    response = client.post("/login/access-token",
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                           data={"username": settings.FIRST_SUPERUSER,
                                 "password": settings.FIRST_SUPERUSER_PASSWORD},
    )
    return response.json()

def test_get_all_trainee():
    token = get_token()["access_token"]
    response = client.get("/trainee", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()[0] == {
        "email": "test@test.com",
        "is_active": True,
        "is_superuser": True,
        "full_name": None,
        "id": 1
    }


def test_get_trainee_by_id():
    token = get_token()["access_token"]
    response = client.get("/trainee/1", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {
        "email": "test@test.com",
        "is_active": True,
        "is_superuser": True,
        "full_name": None,
        "id": 1
    }


def test_get_all_trainee_with_invalid_token():
    response = client.get("/trainee", headers={"Authorization": "Bearer 111111111"})
    assert response.status_code == 403
    assert response.json() == {
        'detail': 'Could not validate credentials'
    }


def test_get_trainee_by_id_with_invalid_token():
    response = client.get("/trainee/1", headers={"Authorization": "Bearer 111111111"})
    assert response.status_code == 403
    assert response.json() == {
        'detail': 'Could not validate credentials'
    }


def test_get_trainee_with_invalid_method():
    response = client.post("/trainee")
    assert response.status_code == 405
    assert response.json() == {
        'detail': 'Method Not Allowed'
    }


def test_get_trainee_without_headers():
    response = client.get("/trainee")
    assert response.status_code == 401
    assert response.json() == {
        'detail': 'Not authenticated'
    }


def test_get_token_with_incorect_data():
    response = client.post("/login/access-token",
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                           data={"username": "111",
                                 "password": "111"},
    )
    assert response.status_code == 400
    assert response.json() == {
        'detail': 'Incorrect email or password'
    }


def test_get_token_with_no_data():
    response = client.post("/login/access-token",
                           headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    assert response.status_code == 422
    assert response.json() == {
        'detail':
            [{'loc':
                  ['body', 'username'],
              'msg': 'field required',
              'type': 'value_error.missing'
              },
             {'loc':
                  ['body', 'password'],
              'msg': 'field required',
              'type': 'value_error.missing'}
             ]}


def test_get_token_with_no_headers():
    response = client.post("/login/access-token",
                           data={"username": "111",
                                 "password": "111"},
    )
    assert response.status_code == 400
    assert response.json() == {
        'detail': 'Incorrect email or password'
    }



