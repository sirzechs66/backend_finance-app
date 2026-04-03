from repositories.transaction_repository import (
    get_transaction_by_id, list_transactions, create_transaction, update_transaction, delete_transaction
)
from core.models import Transaction
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime

def add_transaction(db: Session, user_id: int, amount: float, category: str, type: str, date: datetime, description: str = None) -> Transaction:
    transaction = Transaction(
        user_id=user_id,
        amount=amount,
        category=category,
        type=type,
        date=date,
        description=description
    )
    return create_transaction(db, transaction)

def get_transaction(db: Session, transaction_id: int) -> Optional[Transaction]:
    return get_transaction_by_id(db, transaction_id)

def get_transactions(db: Session, user_id: int, skip: int = 0, limit: int = 20, start_date: datetime = None, end_date: datetime = None, category: str = None, type: str = None) -> List[Transaction]:
    return list_transactions(db, user_id, skip, limit, start_date, end_date, category, type)

def edit_transaction(db: Session, transaction_id: int, data: dict) -> Optional[Transaction]:
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        return None
    return update_transaction(db, transaction, data)

def remove_transaction(db: Session, transaction_id: int) -> bool:
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        return False
    delete_transaction(db, transaction)
    return True
