import streamlit as st
import add_update_ui
import analytics_by_category_ui, analytics_by_month_ui

APP_URL = "http://127.0.0.1:8000/"
st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(['Add/Update Expense', "Analytics by Category", "Analytics by Month"])

with tab1:
    add_update_ui.add_update_tab()
with tab2:
    analytics_by_category_ui.analytics_by_category_tab()
with tab3:
    analytics_by_month_ui.analytics_by_month_tab()