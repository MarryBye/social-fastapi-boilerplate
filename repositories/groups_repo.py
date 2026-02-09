from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from core.alchemy import get_session

class GroupsRepository:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session