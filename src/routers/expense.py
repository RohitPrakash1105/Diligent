from fastapi import APIRouter, HTTPException

from src.models.expenses import Expense, ExpenseCreate


router = APIRouter()


expenses = []

def find_expense(category: str) -> bool:
    return any(expense.category.lower() == category.lower() for expense in expenses)

@router.post("/expenses", response_model=Expense, status_code=201)
def add_expense(expense_data: ExpenseCreate):
    last_id = len(expenses) + 1

    expense = Expense(
        id=last_id,
        **expense_data.model_dump()
    )

    expenses.append(expense)

    return expense

@router.get("/expenses", response_model=list[Expense])
def get_expenses(category: str | None = None):
    if category:
        return [
            expense
            for expense in expenses
            if expense.category.lower() == category.lower()
        ]
    return expenses

@router.get("/expenses/total")
def get_total_expenses():
    total = sum(expense.amount for expense in expenses)

    return {
        "total": total
    }

@router.get("/expenses/total/{category}")
def get_total_by_category(category: str):
    cat = find_expense(category)
    if not cat:
        raise HTTPException(status_code=404, detail="category not found")
    total = 0
    for expense in expenses:
        if expense.category.lower() == category.lower():
            total += expense.amount

    return {
        "category": category,
        "total": total
    }

@router.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: int):
    for expense in expenses:
        if expense.id == expense_id:
            expenses.remove(expense)
            return

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )