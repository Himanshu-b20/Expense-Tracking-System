# Expense Management System

This Expense Tracking System allows users to efficiently manage their personal or business expenses. Users can add and update expense entries, which are securely stored in a MySQL database. The system provides detailed analytics, enabling users to view their spending patterns over a selected time frame or by specific months, helping them make informed financial decisions.

# Techstack
- **Python**
- **Fast API for Backend Development**
- **Streamlit for frontend development**
- **MySQL Db for storing data**

  ![image](https://github.com/user-attachments/assets/7e430087-ba85-493e-90d2-d053a0cf8527)



## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Himanshu-b20/Expense-Tracking-System.git
   ```
2. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
4. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
