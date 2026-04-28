
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou coloque a URL do seu front, ex: ["http://localhost:5173"]
    allow_methods=["*"],
    allow_headers=["*"],
)

from google import genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY não foi definida no arquivo .env")

client = genai.Client(api_key=GEMINI_API_KEY)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=request.question
        )

        return {
            "question": request.question,
            "answer": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))