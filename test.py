# test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_recommendations(client):
    user_id = "3c9e9cf9-aba3-4b50-9e68-a1db779d8dbd"
    response = client.get(f"/recommendations?user_id={user_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert "recommendations" in data
    assert len(data["recommendations"]) > 0
    assert "user_id" in data
    assert data["user_id"] == user_id

def test_invalid_user_id(client):
    response = client.get("/recommendations")
    assert response.status_code == 400
    assert "error" in response.get_json()
