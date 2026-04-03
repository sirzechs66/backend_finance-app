from repositories.dashboard_repository import get_dashboard_aggregates
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from functools import lru_cache

@lru_cache(maxsize=128)
def cached_dashboard(user_id: int, start_date: Optional[str], end_date: Optional[str]):
    # This is a placeholder for in-memory caching; real cache should use a key with all params
    return None

def get_dashboard(db: Session, user_id: int, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
    # Optionally use caching here
    return get_dashboard_aggregates(db, user_id, start_date, end_date)
