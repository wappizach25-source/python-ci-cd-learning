import pytest
from src.app import app, todos, INITIAL_TODOS


@pytest.fixture(autouse=True)
def reset_todos():
    todos.clear()
    todos.extend(todo.copy() for todo in INITIAL_TODOS)


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "To-do API is running"


def test_get_todos():
    client = app.test_client()
    response = client.get("/todos")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_get_single_todo():
    client = app.test_client()
    response = client.get("/todos/1")

    assert response.status_code == 200
    assert response.get_json()["id"] == 1


def test_get_missing_todo():
    client = app.test_client()
    response = client.get("/todos/999")

    assert response.status_code == 404
    assert response.get_json()["error"] == "Todo not found"


def test_create_todo():
    client = app.test_client()
    response = client.post("/todos", json={"title": "Learn GitHub Actions"})

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Learn GitHub Actions"
    assert data["done"] is False


def test_create_todo_without_title():
    client = app.test_client()
    response = client.post("/todos", json={})

    assert response.status_code == 400
    assert response.get_json()["error"] == "Title is required"