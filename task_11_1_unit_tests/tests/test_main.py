import pytest
from fastapi.testclient import TestClient

from main import app, reset_state

client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    reset_state()
    yield
    reset_state()


def test_create_user_success():
    response = client.post("/users", json={"username": "alice", "age": 21})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "username": "alice", "age": 21}


def test_create_user_duplicate():
    client.post("/users", json={"username": "alice", "age": 21})
    response = client.post("/users", json={"username": "alice", "age": 25})
    assert response.status_code == 409
    assert response.json() == {"detail": "User already exists"}


def test_get_existing_user():
    created = client.post("/users", json={"username": "bob", "age": 30}).json()
    response = client.get(f"/users/{created['id']}")
    assert response.status_code == 200
    assert response.json() == created


def test_get_missing_user():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


def test_delete_existing_user():
    created = client.post("/users", json={"username": "carol", "age": 28}).json()
    response = client.delete(f"/users/{created['id']}")
    assert response.status_code == 204
    assert response.content == b""


def test_delete_same_user_twice():
    created = client.post("/users", json={"username": "dave", "age": 32}).json()
    first_response = client.delete(f"/users/{created['id']}")
    second_response = client.delete(f"/users/{created['id']}")
    assert first_response.status_code == 204
    assert second_response.status_code == 404
    assert second_response.json() == {"detail": "User not found"}
