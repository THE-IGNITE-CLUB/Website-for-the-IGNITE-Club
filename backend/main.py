from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This part is CRITICAL: It allows your Website to talk to your Python code
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Later, change this to your specific github.io URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Ignite AI Backend is Online!"}

@app.get("/ask")
def ask_ai(question: str):
    # This is where the LLM integration will live!
    return {"answer": f"The Ignite AI received your question: '{question}'. Integration in progress!"}
import mysql.connector
from fastapi import FastAPI

# This connects Python to your Database
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", # Change this to your DB host later
        user="root",
        password="your_password",
        database="ignite_club"
    )

@app.get("/events")
def get_events():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events
