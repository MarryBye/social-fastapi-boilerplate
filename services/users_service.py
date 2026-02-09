from fastapi import Depends
from repositories.users_repo import UsersRepository

class UsersService:
    def __init__(self, users_repo: UsersRepository = Depends()):
        self.users_repo = users_repo
        
    async def test(self):
        return await self.users_repo.test()