from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user: str
    content: str

messages = []

@app.post("/send_message/")
async def send_message(message: Message):
    messages.append(message)
    return messages

@app.get("/get_messages/")
async def get_messages():
    return messages
