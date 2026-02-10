from sqlalchemy import select, func

async def authenticate(session, login: str, password: str):
    result = await session.execute(
        select(func.authenticate(login, password))
    )
    return result.scalar()