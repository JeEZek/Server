from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# write your data
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:testtask@localhost:5432/platform"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
