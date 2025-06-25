import streamlit as st
from datetime import datetime
import requests

APP_URL = "http://127.0.0.1:8000/"

def add_update_tab():
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility='collapsed')
    response = requests.get(f"{APP_URL}/expenses/{selected_date}")
    if response.status_code == 200:
        expense_list = response.json()
    else:
        st.write("Failed to fecth ", response.status_code)
        expense_list = []

    categories = ['Select Category', 'Rent', 'Food', 'Shopping', 'Entertainment', 'Other']
    expense_new_data = []

    with st.form(key='expense_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        for i in range(5):
            if i < len(expense_list):
                amount = expense_list[i]['amount']
                category = expense_list[i]['category']
                notes = expense_list[i]['notes']
            else:
                amount = 0.0
                category = "Select Category"
                notes = ""
            col1, col2, col3 = st.columns(3)
            with col1:
                amount = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount{i}",
                                         label_visibility='collapsed')
            with col2:
                category = st.selectbox(label="Category", options=categories, index=categories.index(category),
                                        key=f"category{i}", label_visibility='collapsed')
            with col3:
                notes = st.text_input(label="Notes", value=notes, key=f"note{i}", label_visibility='collapsed')

            expense_new_data.append({
                "amount": amount,
                "category": category,
                "notes": notes
            })

        submit = st.form_submit_button()
        if submit:
            filter_data = [data for data in expense_new_data if data['amount'] > 0]
            rsp = requests.post(f"{APP_URL}/expenses/{selected_date}", json=filter_data)
            if rsp.status_code == 200:
                st.success("Expense updated successfully")
            else:
                st.error("Failed to update expense")
