from os import getenv
from dotenv import load_dotenv
from core.exceptions import InvalidEnvironmentFile

class Config:
    debug = True
    env_file = ".env.dev"
        
    class Database:
        host = getenv("DB_HOST")
        port = getenv("DB_PORT")
        user = getenv("DB_USER")
        password = getenv("DB_PASSWORD")
        database = getenv("DB_NAME")
        
    class SQLAlchemy:
        pool_size=10
        max_overflow=20
        timeout=30
        
    class PythonJose:
        secret = getenv("JWT_SECRET")
        algorithm = getenv("JWT_ALGORITHM")
        expiration = getenv("JWT_EXPIRATION_MINUTES")

    class FastAPI:
        title = "Social FastAPI"
        description = "A social media API built with FastAPI"
        version = "1.0.0"
        secret = getenv("FASTAPI_SECRET")

load_dotenv(Config.env_file)

if not Config.env_file:
    raise InvalidEnvironmentFile(f"Environment file '{Config.env_file}' is missing or invalid.")
