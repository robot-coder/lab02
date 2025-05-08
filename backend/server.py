import fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user: str
    text: str

conversation = []

@app.post("/send_message/")
async def send_message(message: Message):
    conversation.append(message)
    # Here you would integrate LiteLLM to get a response
    response = "This is a response from the LLM."
    conversation.append(Message(user="Assistant", text=response))
    return conversation

@app.get("/conversation/")
async def get_conversation():
    return conversation
