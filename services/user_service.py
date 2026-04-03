from repositories.user_repository import (
    get_user_by_id, get_user_by_username, get_user_by_email, create_user, list_users
)
from core.models import User
from sqlalchemy.orm import Session
from modules.auth import hash_password
from typing import Optional

def register_user(db: Session, username: str, email: str, password: str, role: str = "VIEWER") -> User:
    if get_user_by_username(db, username) or get_user_by_email(db, email):
        raise ValueError("Username or email already exists")
    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role=role
    )
    return create_user(db, user)

def get_user(db: Session, user_id: int) -> Optional[User]:
    return get_user_by_id(db, user_id)

def get_users(db: Session, skip: int = 0, limit: int = 20):
    return list_users(db, skip, limit)
