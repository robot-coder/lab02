from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat/")
async def chat(message: Message):
    # Here we would call the LiteLLM API to get a response
    # For now, we will return a mock response
    return {"response": f"You said: {message.user_input}"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Chat Assistant API!"}