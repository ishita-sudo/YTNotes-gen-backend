from flask import request, jsonify
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
api_key=os.getenv("DEEPSEEK_API_KEY")

def generate_notes(topic: str) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type":"application/json"
    }
    prompt =(
        "You are a helpful assistant. Summarize the following transcript into clear, structured notes:\n\n"
        f"{topic}\n\n"
        "Use bullet points, highlight key ideas, and keep it concise."
    )
    payload =(
        {
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    response= requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        content=response.json()["choices"][0]["message"]["content"]
        return content
    else:
        return f"Error {response.status_code}:{response.text}"

    

