from core.models import Transaction
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

def get_transaction_by_id(db: Session, transaction_id: int) -> Optional[Transaction]:
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def list_transactions(db: Session, user_id: int, skip: int = 0, limit: int = 20, start_date: datetime = None, end_date: datetime = None, category: str = None, type: str = None) -> List[Transaction]:
    query = db.query(Transaction).filter(Transaction.user_id == user_id)
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    if category:
        query = query.filter(Transaction.category == category)
    if type:
        query = query.filter(Transaction.type == type)
    return query.order_by(Transaction.date.desc()).offset(skip).limit(limit).all()

def create_transaction(db: Session, transaction: Transaction) -> Transaction:
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def update_transaction(db: Session, transaction: Transaction, data: dict) -> Transaction:
    for key, value in data.items():
        setattr(transaction, key, value)
    db.commit()
    db.refresh(transaction)
    return transaction

def delete_transaction(db: Session, transaction: Transaction):
    db.delete(transaction)
    db.commit()
