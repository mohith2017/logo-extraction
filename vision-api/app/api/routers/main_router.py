from fastapi import APIRouter
from app.api.routers.user import user_router
from app.api.routers.openai import openai_router
from app.api.routers.claude import claude_router
from app.api.routers.logo import logo_router

router = APIRouter()

router.include_router(user_router)
router.include_router(openai_router)
router.include_router(claude_router)
router.include_router(logo_router)
