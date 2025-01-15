from fastapi import APIRouter, HTTPException
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import requests

load_dotenv()
logo_module = APIRouter()

# Logo Link CDN base URL
LOGO_LINK_CDN_URL = "https://cdn.brandfetch.io/{domain}?c={client_id}"

class URLInput(BaseModel):
    urls: list[str]

@logo_module.post("/fetch")
async def fetch_logo_links(url_input: URLInput):
    client_id = os.getenv("BRANDFETCH_CLIENT_ID")  # Ensure you have the client ID in your .env
    if not client_id:
        raise HTTPException(status_code=500, detail="Client ID not found")

    logos = {}
    for url in url_input.urls:
        # Construct the logo link using the provided client ID
        logo_link = LOGO_LINK_CDN_URL.format(client_id=client_id, domain=url)
        logos[url] = logo_link

    return logos
