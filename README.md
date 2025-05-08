# Chat Assistant Documentation

## Overview
This project implements a Chat Assistant using FastAPI for the backend and a simple HTML/JavaScript frontend.

## Setup Instructions
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open `index.html` in your browser to interact with the Chat Assistant.

## Deployment
To deploy the Chat Assistant on Render.com:
1. Create a new web service on Render.
2. Connect your GitHub repository.
3. Set the build command to `pip install -r requirements.txt` and the start command to `uvicorn app.main:app --host 0.0.0.0 --port 10000`.

## API Key
To use OpenRouter.ai, create an API key with a limit of $3.00.

## Features
- Continuous conversation with LLM responses.
- Text input for user messages.
- Display of conversation history.

## Extensions
- Support for text and image file uploads.
- Side-by-side LLM response comparison.
