import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models import Base, Transaction, TransactionTypeEnum
from repositories.dashboard_repository import get_dashboard_aggregates
from datetime import datetime

@pytest.fixture(scope="module")
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

@pytest.fixture
def seed_transactions(db):
    db.add_all([
        Transaction(user_id=1, amount=100, category="Salary", type=TransactionTypeEnum.INCOME, date=datetime(2024, 1, 1)),
        Transaction(user_id=1, amount=50, category="Food", type=TransactionTypeEnum.EXPENSE, date=datetime(2024, 1, 2)),
        Transaction(user_id=1, amount=30, category="Food", type=TransactionTypeEnum.EXPENSE, date=datetime(2024, 1, 3)),
        Transaction(user_id=1, amount=200, category="Bonus", type=TransactionTypeEnum.INCOME, date=datetime(2024, 1, 4)),
    ])
    db.commit()


def test_dashboard_aggregation(db, seed_transactions):
    results = get_dashboard_aggregates(db, user_id=1)
    # Should group by category and type
    result_map = {(r[0], r[1]): r[2] for r in results}
    assert result_map[("Salary", "INCOME")] == 100
    assert result_map[("Food", "EXPENSE")] == 80
    assert result_map[("Bonus", "INCOME")] == 200
