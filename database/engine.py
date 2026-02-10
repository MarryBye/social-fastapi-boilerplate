from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from config import Config

database_url = f"postgresql+asyncpg://{Config.Database.user}:{Config.Database.password}@{Config.Database.host}:{Config.Database.port}/{Config.Database.database}"

engine = create_async_engine(
    url=database_url,
    echo=Config.debug,
    pool_size=Config.SQLAlchemy.pool_size,
    max_overflow=Config.SQLAlchemy.max_overflow,
    pool_recycle=Config.SQLAlchemy.timeout,
)

SessionMaker = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncSession:
    try:
        async with SessionMaker() as session:
            yield session
    except Exception as e:
        print(f"Error occurred while getting session: {e}")
        raise