from fastapi import APIRouter, Request, Response
from fastapi.routing import APIRoute
import time
from typing import Callable

from app.api.endpoints import items, users, flats

# class TimedRoute(APIRoute):
#     def get_route_handler(self) -> Callable:
#         original_route_handler = super().get_route_handler()

#         async def custom_route_handler(request: Request) -> Response:
#             before = time.time()
#             response = await original_route_handler(request)
#             # response: Response = await original_route_handler(request)
#             duration = time.time() - before
#             # response.headers["X-Response-Time"] = str(duration)
#             print(f"route duration: {duration}")
#             # print(f"route response: {response}")
#             # print(f"route response headers: {response.headers}")
#             return response

#         return custom_route_handler

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(flats.router, prefix="/flats", tags=["flats"])
