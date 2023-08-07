from fastapi import APIRouter

from app.api.endpoints import items, users, flats

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(flats.router, prefix="/flats", tags=["flats"])
