import streamlit as st
import requests
import pandas as pd
import calendar

APP_URL = "http://127.0.0.1:8000/"

def analytics_by_month_tab():
    response = requests.get(f"{APP_URL}/analytics/months")
    rsp = response.json()
    month_no = [expense_month['expense_month'] for expense_month in rsp]
    month_names = [calendar.month_name[m] for m in month_no]

    ui_data = {
        "Month": month_no,
        "Month Name": month_names,
        "Total": [expense_month['month_total'] for expense_month in rsp]
    }

    df = pd.DataFrame(ui_data)
    df = df.set_index('Month')
    df.sort_values(by='Total', ascending=False, inplace=True)
    st.title("Expense Breakdown by Months")
    st.bar_chart(data=df.set_index('Month Name')['Total'], width=0, height=0, use_container_width=True)
    df['Total'] = df['Total'].map("Rs. {:,.2f}".format)
    st.table(df)

if __name__ == "__main__":
    analytics_by_month_tab()