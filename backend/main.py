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
