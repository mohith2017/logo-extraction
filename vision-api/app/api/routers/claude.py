from fastapi import APIRouter
from app.api.endpoints.claude.claude import claude_module

claude_router = APIRouter()

# Include the OpenAI Vision API router
claude_router.include_router(
    claude_module,
    prefix="/claude",
    tags=["claude-vision"],
    responses={404: {"description": "Not found"}},
)
