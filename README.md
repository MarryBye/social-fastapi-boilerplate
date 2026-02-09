# FastAPI Web Application Boilerplate

## Overview
This repository is a FastAPI boilerplate for building RESTful web services with async-first patterns and clear separation of concerns. It targets production-ready APIs with token-based authentication, database access, and migration support.

## Project design
The template follows a layered architecture: routers (HTTP endpoints), services/use-cases, repositories/DB access, Pydantic models/schemas, and migrations. Dependency injection uses FastAPI's Depends, and code is organized to make unit testing and async workflows straightforward.

## Environment variables (.env.example)
Example values provided in .env.example:
```
# FastAPI Configuration
FASTAPI_SECRET="your_fastapi_secret"

# JWT configuration
JWT_SECRET="your_jwt_secret"
JWT_ALGORITHM="HS256"
JWT_EXPIRATION_MINUTES="120"

# Database configuration
DB_HOST="localhost"
DB_PORT="5432"
DB_USER="your_user"
DB_PASSWORD="your_password"
DB_NAME="your_db_name"
```
- FASTAPI_SECRET: application-level secret (cookies, CSRF, other secrets).
- JWT_SECRET: symmetric key for signing JWTs.
- JWT_ALGORITHM: algorithm used to sign tokens (e.g., HS256).
- JWT_EXPIRATION_MINUTES: token lifetime in minutes.
- DB_HOST/DB_PORT/DB_USER/DB_PASSWORD/DB_NAME: Postgres connection parameters used to construct DATABASE_URL.

## Configuration file
The config module typically loads environment variables (via python-dotenv or Pydantic BaseSettings) and exposes typed settings to the app. It builds the database URL, provides JWT parameters to the auth utilities, and centralizes secrets (avoid hardcoding). Token creation/validation uses JWT_SECRET, JWT_ALGORITHM and JWT_EXPIRATION_MINUTES; DB access uses the assembled connection string from the DB_* variables.

## Technology stack (typical requirements.txt)
Common dependencies you will find in requirements.txt for this boilerplate:
- fastapi, uvicorn (ASGI server)
- pydantic (settings and schemas)
- sqlalchemy (ORM) plus an async DB driver (asyncpg or psycopg2-binary for PostgreSQL)
- alembic (migrations)
- python-dotenv (load .env in development)
- python-jose (JWT handling) and passlib (password hashing)
- testing tools (pytest, httpx) and typing/dev helpers

Each dependency maps to a layer (web, auth, db, migrations, testing) and can be adjusted depending on sync vs async choices.

## Notes
Keep secrets out of version control, use the .env.example as a template, and prefer environment-based configuration in production (e.g., container secrets or cloud secret managers).