from sqlalchemy.orm import Session

from models import models
from models.models import Client


def get_clients(db: Session):
    return db.query(models.Client).all()


def add_client(db: Session, name: str):
    new_client = Client(name=name)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client
