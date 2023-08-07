
from fastapi import Depends, FastAPI
from starlette.middleware.cors import CORSMiddleware
#from fastapi.logger import logger
import logging

from app.api.api import api_router
from app.core.config import settings

from .dependencies import get_query_token, get_token_header
# from .internal import admin
# from .routers import items, users

# logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)


# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# logger = logging.getLogger("uvicorn.error")
logger = logging.getLogger(__name__)
logger.info("Initializing app...")


app = FastAPI()
# app = FastAPI(dependencies=[Depends(get_query_token)])

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix="/api")
# app.include_router(users.router)
# app.include_router(items.router)
# # app.include_router(
# #     admin.router,
# #     prefix="/admin",
# #     tags=["admin"],
# #     dependencies=[Depends(get_token_header)],
# #     responses={418: {"description": "I'm a teapot"}},
# # )


@app.get("/")
async def root():
    # logger.info("def root")
    return {"message": "Hello Bigger Applications!"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8002, debug=True, reload=False)