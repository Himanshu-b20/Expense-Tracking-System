from backend import db_helper

def test_fetch_expenses_by_date():
    expenses = db_helper.fetch_expenses_by_date("2024-08-15")
    assert len(expenses) == 1