# Chat Assistant Documentation

## Overview
This project implements a Chat Assistant using FastAPI for the backend and a simple HTML/JavaScript frontend. The assistant allows users to interact with different LLMs and compare their responses.

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/robot-coder/lab02.git
   cd lab02
   ```
2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn requests
   ```
4. **Set your OpenRouter API Key**:
   ```bash
   export OPENROUTER_API_KEY='your_api_key_here'
   ```

## Usage Examples
1. **Run the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```
2. **Access the API**:
   Open your browser and go to `http://127.0.0.1:8000/docs` to see the API documentation.

3. **Send a message to the Chat Assistant**:
   Use the `/chat/` endpoint to send a message and receive a response.
   ```json
   POST /chat/
   {
       "user_input": "Hello, how are you?"
   }
   ```

4. **Compare responses from two LLMs**:
   Use the `/compare/` endpoint to compare responses from two different LLMs.
   ```json
   POST /compare/
   {
       "user_input": "Tell me a joke."
   }
   ```

## API Reference
- **POST /chat/**: Sends a user input to the LLM and returns a response.
- **POST /compare/**: Compares responses from two LLMs based on the same user input.
- **POST /upload/text/**: Uploads a text file to enhance the conversation context.
- **POST /upload/image/**: Uploads an image file for multimodal LLMs.

## Architectural Overview
The Chat Assistant consists of a FastAPI backend that handles user requests and a simple HTML/JavaScript frontend that allows users to interact with the assistant. The backend communicates with the OpenRouter API to fetch responses from the LLMs.

## Extensions
- Text file uploads to add context to the conversation.
- Image file uploads for multimodal interactions.
- Side-by-side comparison of responses from different LLMs.

## License
This project is licensed under the MIT License.