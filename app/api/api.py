from fastapi import APIRouter
from app.api.endpoints import trainee, login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(trainee.router, prefix="/trainee", tags=["trainee"])