from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from ai_engine import generate_response

app = FastAPI()

# ✅ ADD THIS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestModel(BaseModel):
    mode: str
    query: str

@app.post("/chat")
def chat(request: RequestModel):
    response = generate_response(request.mode, request.query)

    return {
        "mode": request.mode,
        "response": response
    }