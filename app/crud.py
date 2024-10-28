from sqlmodel import Session, select, delete, func
from app.models import User, UserRegister, UserUpdate, Users
from app.database import SessionDep

def read_users(session: SessionDep):
    pass

def create_user():
    pass

def get_user():
    pass

def update_user():
    pass