from sqlalchemy.orm import Session
from sqlalchemy import func
from core.models import Transaction
from datetime import datetime
from typing import Optional

def get_dashboard_aggregates(db: Session, user_id: int, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
    query = db.query(
        Transaction.category,
        Transaction.type,
        func.sum(Transaction.amount).label("total")
    ).filter(Transaction.user_id == user_id)
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    query = query.group_by(Transaction.category, Transaction.type)
    return query.all()
