from fastapi import APIRouter, Depends
from services.users_service import UsersService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users(service: UsersService = Depends()):
    return await service.test()