from fastapi.testclient import TestClient
from src.main import app
from src.routers.expense import expenses

client = TestClient(app)


def setup_function():
    expenses.clear()


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Pizza"
    assert data["amount"] == 300
    assert data["category"] == "Food"
    assert data["date"] == "2026-08-02"
    assert "id" in data


def test_get_all_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    response = client.get("/expenses")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_by_category():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Bus Ticket",
            "amount": 50,
            "category": "Transport",
            "date": "2026-08-02",
        },
    )

    response = client.get("/expenses?category=Food")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["category"] == "Food"


def test_total_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Bus Ticket",
            "amount": 50,
            "category": "Transport",
            "date": "2026-08-02",
        },
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200
    assert response.json()["total"] == 350


def test_total_by_category():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    client.post(
        "/expenses",
        json={
            "title": "Burger",
            "amount": 200,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    response = client.get("/expenses/total/Food")

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Food"
    assert data["total"] == 500


def test_delete_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 300,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    expense_id = response.json()["id"]

    response = client.delete(f"/expenses/{expense_id}")

    assert response.status_code == 204

    response = client.get("/expenses")

    assert len(response.json()) == 0


def test_delete_non_existing_expense():
    response = client.delete("/expenses/999")

    assert response.status_code == 404


def test_invalid_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": -100,
            "category": "Food",
            "date": "2026-08-02",
        },
    )

    assert response.status_code == 422
