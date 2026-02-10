from fastapi import FastAPI
from database.engine import engine
from database.tables import metadata

from api import router as api_router
from config import Config

app = FastAPI(
    debug=Config.debug
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        for schema in Config.SQLAlchemy.reflected_schemas:
            await conn.run_sync(
                lambda sync_conn: metadata.reflect(sync_conn, schema=schema, extend_existing=True)
            )
app.include_router(api_router)
