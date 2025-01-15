import json
import os
import base64
from fastapi import APIRouter, HTTPException, UploadFile, File
from dotenv import load_dotenv
import anthropic

load_dotenv()

claude_module = APIRouter()

# Set the Anthropic API key globally
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
if not anthropic_api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment variables")

@claude_module.post("/vision")
async def call_claude_vision_api(image: UploadFile = File(...)):
    client = anthropic.Anthropic(api_key=anthropic_api_key)

    text_generation_prompt = """Select all logos from the image and place it in a 
    list where each logo is replaced with the website link with {sample.com} format based on the logo. Return only this 
    list in the python readable format."""

    image_data = await image.read()
    
    # Convert the image data to base64
    image_media_type = image.content_type  
    image_data_base64 = base64.standard_b64encode(image_data).decode("utf-8")

    # Prepare the messages for the API call
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data_base64,
                    },
                },
                {
                    "type": "text",
                    "text": text_generation_prompt
                }
            ],
        }
    ]

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            messages=messages
        )

        logos_list = []
        if hasattr(response, 'content') and isinstance(response.content, list):
            for item in response.content:
                if hasattr(item, 'text'):
                    # Extract the text which contains the list of URLs
                    text_content = item.text
                    print(text_content)
                    start_index = text_content.find('[')
                    end_index = text_content.find(']')
                    if start_index != -1 and end_index != -1:
                        logos_list_str = text_content[start_index:end_index + 1]
                        logos_list = eval(logos_list_str) 


        return logos_list
    
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
