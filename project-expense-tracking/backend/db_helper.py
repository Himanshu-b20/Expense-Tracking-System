import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logging

logger = setup_logging("db_helper")

@contextmanager
def db_cursor(commit = False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rootAdmin",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
            connection.commit()
    cursor.close()
    connection.close()

def fetch_expenses_by_date(expense_date):
    logger.info(f"Inside fetch_expenses_by_date on date : {expense_date}")
    with db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def delete_expenses_by_date(expense_date):
    logger.info(f"Inside delete_expenses_by_date on date : {expense_date}")
    with db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s", (expense_date,))


def insert_expenses(expense_date, amount, category, notes):
    logger.info(f"Inside insert_expenses and data is : {expense_date}, {amount}, {category}, {notes}")
    with db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",(expense_date, amount, category, notes))

def fetch_expense_summary(expense_date1, expense_date2):
    logger.info(f"Inside fetch_expense_summary between dates: {expense_date1}, {expense_date2}")
    with db_cursor() as cursor:
        cursor.execute("SELECT category, sum(amount) as total from expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category;",(expense_date1, expense_date2))
        data = cursor.fetchall()
        return data

def fetch_expense_summary_month():
    logger.info(f"Inside fetch_expense_summary_month between dates")
    with db_cursor() as cursor:
        cursor.execute("SELECT MONTH(expense_date) AS expense_month, sum(amount) AS month_total FROM expense_manager.expenses GROUP BY MONTH(expense_date)")
        data = cursor.fetchall()
        return data


if __name__ == "__main__":
    data = fetch_expense_summary_month()
    print(data)

