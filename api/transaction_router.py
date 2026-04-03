
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.db import get_db
from services.transaction_service import add_transaction, get_transaction, get_transactions, edit_transaction, remove_transaction
from schemas.transaction_schema import TransactionCreate, TransactionOut
from typing import List, Optional
from datetime import datetime
from modules.dependencies import get_current_user
from core.models import User


router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=TransactionOut, status_code=status.HTTP_201_CREATED)
def create_transaction(
    transaction_in: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return add_transaction(db, current_user.id, transaction_in.amount, transaction_in.category, transaction_in.type, transaction_in.date, transaction_in.description)

@router.get("/{transaction_id}", response_model=TransactionOut)
def read_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transaction = get_transaction(db, transaction_id)
    if not transaction or transaction.user_id != current_user.id:
        raise HTTPException(status_code=404, detail={"error": {"code": "not_found", "message": "Transaction not found", "details": None}})
    return transaction

@router.get("/", response_model=List[TransactionOut])
def list_transactions(
    skip: int = 0,
    limit: int = 20,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    category: Optional[str] = None,
    type: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_transactions(db, current_user.id, skip, limit, start_date, end_date, category, type)
