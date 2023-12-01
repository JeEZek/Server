from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.clients import get_clients, add_client
from database.database import get_db
from schemes import schemes

router = APIRouter()


@router.get("", response_model=list[schemes.Client])
def read_clients(db: Session = Depends(get_db)):
    clients = get_clients(db)
    return clients


@router.post("/create", response_model=schemes.Client)
def create_client(name: str, db: Session = Depends(get_db)):
    client = add_client(db, name)
    return client
