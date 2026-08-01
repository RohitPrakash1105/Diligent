from fastapi import FastAPI
from .routers.expense import router as expense_router

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0"
)

app.include_router(expense_router)