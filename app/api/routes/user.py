from fastapi import APIRouter
from app.models import (
    User,
    Users,
    UserRegister,
    UpdatePassword,
    UserUpdate
)
from sqlmodel import Session, select, delete, func
from app.database import SessionDep

router = APIRouter()

@router.get(
    "/",
    response_model=Users
)
def get_all_users(session: SessionDep):
    pass

@router.post("/")
def register(user:User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/{id}")
def get_user(user:User):
    pass

@router.put("/{id}")
def update_user(user:UserUpdate):
    pass

@router.delete("/{id}")
def delete_user():
    pass