from fastapi import APIRouter
from app.models import UserLogin
router = APIRouter()

@router.post("/login")
def login(user:UserLogin):
    pass