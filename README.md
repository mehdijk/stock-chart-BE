# Stock Price Chart Web App - Backend

## Setup Instructions:

1. **Clone the Repository:**
   ```
   git clone https://github.com/mehdijk/stock-chart-BE.git
   cd stock-chart-BE
   ```

2. **Create and Activate Virtual Environment:**
   ```
   python -m venv venv
   source venv/bin/activate    # For Unix/Linux
   venv\Scripts\activate       # For Windows
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Running the Backend Server:

1. **Navigate to the `stock-chart-BE` directory:**
   ```
   cd stock-chart-BE
   ```

2. **Run the FastAPI server:**
   ```
   uvicorn main:app --reload
   ```

3. **Accessing the Backend:**

   - The backend server should now be running on `http://localhost:8000`.
   - Use this URL to interact with the backend API endpoints.

