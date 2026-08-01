
# AI Usage Notes

# 1. AI-Generated vs. Self-Written Code

## AI-Assisted Components

The following parts were initially generated or suggested by AI:

- Initial Pydantic model definitions
- FastAPI route structure
- CRUD endpoint implementations
- Initial pytest test suite
- Swagger/OpenAPI setup guidance

---

## Changes Made to AI-Generated Code

### 1. Refactored the Pydantic Models

The AI initially generated two separate models with duplicated fields.

```python
class ExpenseCreate(BaseModel):
    title: str
    amount: float = Field(gt=0)
    category: str
    date: date


class Expense(BaseModel):
    id: int
    title: str
    amount: float = Field(gt=0)
    category: str
    date: date
```

I refactored this by making `Expense` inherit from `ExpenseCreate`.

```python
class Expense(ExpenseCreate):
    id: int
```

**Reason**

This removes duplicated fields, keeps the models easier to maintain, and follows the DRY (Don't Repeat Yourself) principle.

---

### 2. Combined Two GET Endpoints into One

The AI initially suggested two different endpoints.

```python
GET / expenses
GET / expenses / {category}
```

I replaced them with a single endpoint that accepts an optional query parameter.

```python
GET /expenses
GET /expenses?category=Food
```

**Reason**

- Cleaner REST API design
- Fewer endpoints to maintain
- More flexible filtering
- Case-insensitive category matching

---

### 3. Added Error Handling for Invalid Categories

The original implementation assumed that the requested category always existed.

I added explicit validation before calculating totals.

```python
if not find_expense(category):
    raise HTTPException(status_code=404, detail="Category not found")
```

**Reason**

Returning a 404 response clearly indicates that the requested category does not exist instead of returning an incorrect result.

---

### 4. Simplified Expense IDs

The AI initially generated UUID-based identifiers.

```python
id: UUID = Field(default_factory=uuid4)
```

Since this project stores data only in memory, I replaced UUIDs with incrementing integer IDs.

```python
last_id = len(expenses) + 1
expense = Expense(id=last_id, **expense_data.model_dump())
```

**Reason**

- Simpler implementation
- Easier manual testing
- Easier endpoint testing
- Better suited for an in-memory application without a database

---

### 5. Simplified the Test Suite

The AI generated asynchronous tests using:

- AsyncClient
- ASGITransport
- pytest.mark.anyio

I replaced them with FastAPI's synchronous `TestClient`.

```python
client = TestClient(app)
```

**Reason**

My API only contains synchronous endpoints and uses in-memory storage, so asynchronous testing added unnecessary complexity.

---

### 6. Added an Additional Edge Case

The AI-generated tests verified successful requests but did not verify the behaviour when requesting totals for a non-existent category.

I added the following test:

```python
def test_total_non_existing_category():
    response = client.get("/expenses/total/Education")

    assert response.status_code == 404
```

**Reason**

This validates an important edge case and ensures the API returns the expected HTTP 404 response.

---

# 2. Validation Performed

Every AI-generated suggestion was reviewed before being accepted.

The following validation steps were performed:

- Manually tested every endpoint using Postman.
- Verified request and response models using Swagger UI.
- Executed the complete pytest test suite.
- Confirmed that invalid inputs return the expected HTTP status codes.
- Verified filtering, deletion, and total calculation logic using multiple test cases.

---

# 3. AI Suggestions Not Used

The following AI suggestions were intentionally not adopted:

- Docker support was not implemented because Swagger/OpenAPI documentation was selected as the optional bonus feature.
- Additional endpoints (such as expense existence or search endpoints) were omitted since they were outside the assignment requirements.
- Database integration was intentionally avoided because the assignment explicitly allowed in-memory storage.