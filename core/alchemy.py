from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from config import Config

ENGINE = create_async_engine(
    f"postgresql+asyncpg://{Config.Database.user}:{Config.Database.password}@{Config.Database.host}:{Config.Database.port}/{Config.Database.database}",
    echo=Config.debug,
    pool_size=Config.SQLAlchemy.pool_size,
    max_overflow=Config.SQLAlchemy.max_overflow,
    timeout=Config.SQLAlchemy.timeout,
)

SessionMaker = async_sessionmaker(ENGINE, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with SessionMaker() as session:
        yield session