
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.db import get_db
from services.user_service import register_user, get_user, get_users
from schemas.user_schema import UserCreate, UserOut
from core.models import User
from typing import List
from modules.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    try:
        user = register_user(db, user_in.username, user_in.email, user_in.password, user_in.role.value)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail={"error": {"code": "user_exists", "message": str(e), "details": None}})

@router.get("/{user_id}", response_model=UserOut)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail={"error": {"code": "not_found", "message": "User not found", "details": None}})
    # Only allow users to see their own info or if admin
    if user.id != current_user.id and current_user.role.value != "ADMIN":
        raise HTTPException(status_code=403, detail={"error": {"code": "forbidden", "message": "Insufficient permissions", "details": None}})
    return user

@router.get("/", response_model=List[UserOut])
def list_users(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only admin can list all users
    if current_user.role.value != "ADMIN":
        raise HTTPException(status_code=403, detail={"error": {"code": "forbidden", "message": "Insufficient permissions", "details": None}})
    return get_users(db, skip, limit)
