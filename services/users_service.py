from fastapi import Depends
from database.repositories.users_repo import UsersRepository
from database.functions import authenticate

class UsersService:
    def __init__(self, users_repo: UsersRepository = Depends()):
        self.users_repo = users_repo

    async def authenticate(self, login: str, password: str):
        return await authenticate(self.users_repo.session, login, password)
    
    async def all(self):
        return await self.users_repo.all()

    async def get(self, user_id: int):
        return await self.users_repo.get(user_id)

    async def create(self, **kwargs):
        return await self.users_repo.create(**kwargs)

    async def update(self, user_id: int, **kwargs):
        return await self.users_repo.update(user_id, **kwargs)

    async def delete(self, user_id: int):
        return await self.users_repo.delete(user_id)