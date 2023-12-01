from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# write your datas
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:testtask@localhost:5432/test3"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
