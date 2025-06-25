import streamlit as st
from datetime import datetime
import requests
import pandas as pd
from keras.src.losses import hinge

APP_URL = "http://127.0.0.1:8000/"

def analytics_by_category_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{APP_URL}/analytics", json= payload)
        rsp = response.json()

        ui_data = {
            "Category": list(rsp.keys()),
            "Total":[rsp[category]['total'] for category in rsp],
            "Percentage": [rsp[category]['percentage'] for category in rsp]
        }
        df = pd.DataFrame(ui_data)
        df = df.set_index('Category')
        df.sort_values(by = 'Total',ascending=False,inplace=True)
        st.title("Expense Breakdown by Category")
        st.bar_chart(data=df['Total'], width = 0, height = 0,use_container_width=True)

        df['Total'] = df['Total'].map("Rs. {:,.2f}".format)
        df['Percentage'] = df['Percentage'].map("{:,.2f} %".format)
        st.table(df)
if __name__ == "__main__":
    analytics_by_category_tab()

