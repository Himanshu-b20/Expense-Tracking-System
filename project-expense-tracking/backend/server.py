from fastapi import FastAPI, HTTPException
import db_helper
from datetime import date
from typing import List
from pydantic import BaseModel
import uvicorn


class Expense(BaseModel):
    amount : float
    category : str
    notes : str

class DateRange(BaseModel):
    start_date : date
    end_date : date

app = FastAPI()


@app.get("/expenses/{expense_date}", response_model = List[Expense])
def get_expenses(expense_date : date):
    expenses = db_helper.fetch_expenses_by_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="No data found")
    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date : date, expenses: List[Expense]):
    db_helper.delete_expenses_by_date(expense_date)
    for ex in expenses:
        db_helper.insert_expenses(expense_date, ex.amount, ex.category, ex.notes)
    return {"message" : "Expense updated Successfully!!"}

@app.post("/analytics")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="No analytics data found")
    grand_total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/grand_total)*100 if grand_total > 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown

@app.get("/analytics/months")
def get_analytics():
    data = db_helper.fetch_expense_summary_month()
    if data is None:
        raise HTTPException(status_code=500, detail="No analytics data found")
    return data

# if __name__ == "__main__":
#     uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)