
from pydantic import BaseModel, constr, condecimal
from enum import Enum
from typing import Optional, Annotated
from datetime import datetime

class TransactionTypeEnum(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"

class TransactionCreate(BaseModel):
    amount: float
    category: Annotated[str, constr(min_length=1, max_length=50)]
    type: TransactionTypeEnum
    date: datetime
    description: Optional[str] = None

class TransactionOut(BaseModel):
    id: int
    amount: float
    category: str
    type: TransactionTypeEnum
    date: datetime
    description: Optional[str]
    class Config:
        from_attributes = True
