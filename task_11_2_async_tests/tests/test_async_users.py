import pytest
from faker import Faker
from httpx import ASGITransport, AsyncClient

from main import app, reset_state

fake = Faker()


@pytest.fixture(autouse=True)
def clear_db():
    reset_state()
    yield
    reset_state()


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as async_client:
        yield async_client


@pytest.mark.asyncio
async def test_create_user(client):
    payload = {"username": fake.user_name(), "age": fake.random_int(min=19, max=80)}
    response = await client.post("/users", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["id"] == 1
    assert data["username"] == payload["username"]
    assert data["age"] == payload["age"]


@pytest.mark.asyncio
async def test_get_existing_user(client):
    payload = {"username": fake.user_name(), "age": fake.random_int(min=19, max=80)}
    created = await client.post("/users", json=payload)
    user_id = created.json()["id"]
    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"id": user_id, **payload}


@pytest.mark.asyncio
async def test_get_missing_user(client):
    response = await client.get("/users/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}


@pytest.mark.asyncio
async def test_delete_existing_user(client):
    payload = {"username": fake.user_name(), "age": fake.random_int(min=19, max=80)}
    created = await client.post("/users", json=payload)
    user_id = created.json()["id"]
    response = await client.delete(f"/users/{user_id}")
    assert response.status_code == 204
    assert response.content == b""


@pytest.mark.asyncio
async def test_delete_same_user_twice(client):
    payload = {"username": fake.user_name(), "age": fake.random_int(min=19, max=80)}
    created = await client.post("/users", json=payload)
    user_id = created.json()["id"]
    first_response = await client.delete(f"/users/{user_id}")
    second_response = await client.delete(f"/users/{user_id}")
    assert first_response.status_code == 204
    assert second_response.status_code == 404
    assert second_response.json() == {"detail": "User not found"}


@pytest.mark.asyncio
async def test_create_user_invalid_payload(client):
    response = await client.post("/users", json={"username": fake.user_name(), "age": "wrong"})
    assert response.status_code == 422
