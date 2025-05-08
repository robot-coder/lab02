from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
import requests
import os

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

@app.post("/upload-text/")
async def upload_text(file: UploadFile = File(...)):
    content = await file.read()
    # Process the text file content here
    return {"filename": file.filename, "content": content.decode('utf-8')}

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    content = await file.read()
    # Process the image file content here
    return {"filename": file.filename, "message": "Image uploaded successfully"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Chat Assistant API!"}