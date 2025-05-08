import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class Message(BaseModel):
    user_input: str

@app.post("/chat/")
async def chat(message: Message):
    # Call the LiteLLM API to get a response
    api_key = os.getenv('OPENROUTER_API_KEY')
    response = requests.post(
        'https://api.openrouter.ai/v1/chat',
        headers={'Authorization': f'Bearer {api_key}'},
        json={'prompt': message.user_input}
    )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error calling LLM")
    return response.json()

@app.get("/")
async def root():
    return {"message": "Welcome to the Chat Assistant API!"}