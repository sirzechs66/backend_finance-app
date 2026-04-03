from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from core.db import get_db
from services.user_service import register_user
from repositories.user_repository import get_user_by_username
from schemas.user_schema import UserCreate, UserOut
from modules.auth import verify_password, create_access_token
import logging

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db), request: Request = None):
    logger = logging.getLogger("app")
    try:
        user = register_user(db, user_in.username, user_in.email, user_in.password, user_in.role.value)
        return user
    except ValueError as e:
        logger.error(f"Registration error for {user_in.email}: {str(e)}")
        raise HTTPException(status_code=400, detail={"error": {"code": "user_exists", "message": str(e), "details": None}})
    except Exception as e:
        logger.error(f"Registration error for {user_in.email}: {str(e)}")
        raise HTTPException(status_code=400, detail={"error": {"code": "registration_failed", "message": str(e), "details": None}})

@router.post("/login")
def login(data: dict, db: Session = Depends(get_db), request: Request = None):
    logger = logging.getLogger("app")
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        logger.error("Login error: Username and password required")
        raise HTTPException(status_code=400, detail={"error": {"code": "missing_fields", "message": "Username and password required", "details": None}})
    user = get_user_by_username(db, username)
    if not user:
        logger.error(f"Login error: User not found for username {username}")
        raise HTTPException(status_code=401, detail={"error": {"code": "invalid_credentials", "message": "Invalid username or password", "details": None}})
    try:
        if not verify_password(password, user.password_hash):
            logger.error(f"Login error: Invalid password for user {username}")
            raise HTTPException(status_code=401, detail={"error": {"code": "invalid_credentials", "message": "Invalid username or password", "details": None}})
    except ValueError as e:
        logger.error(f"Login error: {str(e)} for user {username}")
        raise HTTPException(status_code=400, detail={"error": {"code": "password_error", "message": str(e), "details": None}})
    access_token = create_access_token({"sub": str(user.id), "username": user.username, "role": user.role.value})
    return {"access_token": access_token, "token_type": "bearer", "user": {"id": user.id, "username": user.username, "email": user.email, "role": user.role.value}}
