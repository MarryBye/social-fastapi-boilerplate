from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete, update, func
from fastapi import Depends
from core.alchemy import get_session

class UsersRepository:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
        
    async def test(self):
        query = select(1)
        result = await self.session.execute(query)
        return result.scalar()
