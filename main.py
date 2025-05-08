@app.post("/compare/")
async def compare_responses(message: Message):
    api_key = os.getenv('OPENROUTER_API_KEY')
    response1 = requests.post(
        'https://api.openrouter.ai/v1/chat',
        headers={'Authorization': f'Bearer {api_key}'},
        json={'prompt': message.user_input}
    )
    response2 = requests.post(
        'https://api.openrouter.ai/v1/chat',
        headers={'Authorization': f'Bearer {api_key}'},
        json={'prompt': message.user_input}
    )
    if response1.status_code != 200 or response2.status_code != 200:
        raise HTTPException(status_code=400, detail="Error calling LLM")
    return {
        "response1": response1.json(),
        "response2": response2.json()
    }