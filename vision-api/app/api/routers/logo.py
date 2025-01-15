from fastapi import APIRouter
from app.api.endpoints.logo.logo import logo_module

logo_router = APIRouter()

# Include the Logo API router
logo_router.include_router(
    logo_module,
    prefix="/logo",
    tags=["logo-fetch"],
    responses={404: {"description": "Not found"}},
)
