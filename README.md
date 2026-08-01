# Smart Expense Tracker API

A RESTful API built with **FastAPI** to manage personal expenses. The application allows users to create, retrieve, filter, calculate totals, and delete expenses. Data is stored **in memory**, making it lightweight and easy to run without requiring a database.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Interactive Swagger/OpenAPI documentation

---

## Tech Stack

- Python 3.x
- FastAPI
- Pydantic
- Pytest
- Uvicorn

---

## Project Structure

```
.
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── expenses.py
│   └── routers
│       ├── __init__.py
│       └── expense.py
└── tests
    └── test_expense.py
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/RohitPrakash1105/Diligent.git
cd Diligent
```

Create a virtual environment (optional but recommended):

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the FastAPI application:

```bash
uvicorn src.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation (Bonus)

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Running the Test Suite

Execute all tests using:

```bash
pytest -v
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | Retrieve all expenses |
| GET | `/expenses?category={category}` | Filter expenses by category |
| GET | `/expenses/total` | Get total expenses |
| GET | `/expenses/total/{category}` | Get total expenses for a category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Sample Request

### Create Expense

**POST** `/expenses`

```json
{
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-08-03"
}
```

### Sample Response

```json
{
    "id": 1,
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-08-03"
}
```

---

## Notes

- Data is stored **in memory** and will be reset whenever the server restarts.
- No external database is required.
- Interactive API documentation is automatically generated using FastAPI's OpenAPI support.

---

## AI Usage

This project was developed with AI assistance. Details regarding AI usage, validation, and modifications are documented in **AI_NOTES.md**.

---

## Author

**Rohit Prakash**

Software Engineering Apprenticeship Assignment
