
# Import all models so Base.metadata.create_all sees all tables
from core.db import Base, engine
import core.models

if __name__ == "__main__":
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("Done.")
