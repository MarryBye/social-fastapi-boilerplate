from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete, update, text
from fastapi import Depends
from database.engine import get_session
from database.tables import users
from datetime import date
from core.types import Gender


class UsersRepository:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session
        
    async def all(self):
        result = await self.session.execute(
            select(users)
        )
        return [row._mapping for row in result]
    
    async def get(self, user_id: int):
        result = await self.session.execute(
            select(users).where(users.columns.id == user_id)
        )
        return result.scalar()
    
    async def create(
        self, 
        login: str, 
        password: str, 
        username: str, 
        first_name: str, 
        last_name: str, 
        date_of_birth: date,
        gender: Gender,
        city_id: int,
        phone_code_country_id: int,
        phone: str,
        email: str
    ):
        result = await self.session.execute(
            insert(users).values(
                login=login,
                password=password,
                username=username,
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                gender=gender,
                city_id=city_id,
                phone_code_country_id=phone_code_country_id,
                phone=phone,
                email=email
            )
        )
        
        await self.session.commit()
        return result

    async def update(self, user_id: int, **kwargs):
        result = await self.session.execute(
            update(users).where(users.columns.id == user_id).values(**kwargs)
        )
        await self.session.commit()
        return result

    async def delete(self, user_id: int):
        result = await self.session.execute(
            delete(users).where(users.columns.id == user_id)
        )
        await self.session.commit()
        return result