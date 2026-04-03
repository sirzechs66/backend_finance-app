from pydantic import BaseModel, EmailStr, constr
from enum import Enum
from typing import Optional

class RoleEnum(str, Enum):
    VIEWER = "VIEWER"
    ANALYST = "ANALYST"
    ADMIN = "ADMIN"

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)
    email: EmailStr
    password: constr(min_length=8, max_length=128)
    role: Optional[RoleEnum] = RoleEnum.VIEWER

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum
    class Config:
        from_attributes = True
