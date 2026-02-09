from fastapi import APIRouter
from api.v1.users import router as users_router
from api.v1.groups import router as groups_router

router = APIRouter(
    prefix="/v1",
    tags=["v1"]
)
router.include_router(users_router)
router.include_router(groups_router)