from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv
import requests

load_dotenv()
openai_module = APIRouter()

# OpenAI API endpoint
OPENAI_VISION_API_URL = "https://api.openai.com/v1/images/generations"

@openai_module.post("/vision")
async def call_openai_vision_api(image_data: dict):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not found")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "dall-e-3",  # Specify the model
        "prompt": image_data.get("image", "") + image_data.get("prompt", ""),  
        "n": 1,  
        "size": "1024x1024"  
    }

    try:
        response = requests.post(OPENAI_VISION_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.HTTPError as err:
        raise HTTPException(status_code=response.status_code, detail=str(err))
