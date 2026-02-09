from fastapi import APIRouter
from services.groups_service import GroupsService

router = APIRouter(
    prefix="/groups",
    tags=["groups"]
)

@router.get("/")
def get_groups():
    return {"groups": ["group1", "group2", "group3"]}