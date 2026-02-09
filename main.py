from fastapi import FastAPI
from config import Config
from api import router as api_router

app = FastAPI(
    debug=Config.debug
)

app.include_router(api_router)
