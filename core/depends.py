from fastapi import Depends
from core.jose import JWTHandler
from services.users_service import UsersService

async def get_current_user(token: str, service: UsersService = Depends()) -> dict:
    payload = JWTHandler.decode_token(token)
    user_id = payload.get("user_id")
    if user_id:
        return await service.get_user_by_id(user_id)
    return None