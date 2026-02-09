from fastapi import APIRouter
from services.users_service import UsersService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_users():
    return {"users": ["user1", "user2", "user3"]}