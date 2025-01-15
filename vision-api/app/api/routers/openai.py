from fastapi import APIRouter
from app.api.endpoints.openai.openai import openai_module

openai_router = APIRouter()

# Include the OpenAI Vision API router
openai_router.include_router(
    openai_module,
    prefix="/openai",
    tags=["openai-vision"],
    responses={404: {"description": "Not found"}},
)
