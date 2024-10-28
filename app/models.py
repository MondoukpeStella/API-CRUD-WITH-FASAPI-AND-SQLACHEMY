from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
import uuid
from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    CREATOR = "creator"
    USER = "user"
    
class Gender(Enum):
    HOMME = "homme"
    FEMME = "femme"

class User(SQLModel, table=True):
    id: uuid.UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    full_name: str = Field(min_length=3, max_length=255)
    telephone: str = Field(unique=True, index=True, max_length=255)
    adress:str
    password: str
    is_active: bool = False
    role: str = Field(default="user")
    
class Users(SQLModel):
    data: list[User]
    count: int
    
class UserRegister(SQLModel):
    full_name:str = Field(default=None, max_length=255)
    telephone: str
    adress: str
    password: str
    
class UserLogin(SQLModel):
    full_name: str = Field(default=None, max_length=255)
    password: str = Field(default=None, max_length=255)
    
class UserUpdate(SQLModel):
    full_name: str | None = Field(default=None, max_length=255)
    adress: str | None = Field(default=None, max_length=255)
    telephone: str | None = Field(default=None, max_length=255)
    is_active: bool | None = Field(default=Role.USER)
    
class UpdatePassword(SQLModel):
    current_password: str = Field(min_length=8, max_length=40)
    new_password: str = Field(min_length=8, max_length=40)

class ClientUpdate(SQLModel):
    pass
