from fastapi import APIRouter

from app.api.routes import authentication, users


router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")