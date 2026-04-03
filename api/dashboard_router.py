from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.db import get_db
from services.dashboard_service import get_dashboard
from typing import Optional
from datetime import datetime
from modules.dependencies import get_current_user
from core.models import User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/")
def dashboard(
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_dashboard(db, current_user.id, start_date, end_date)
