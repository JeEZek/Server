from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.clients import get_clients, add_client, delete_client
from database.database import get_db
from schemes import schemes

router = APIRouter()


@router.get("", response_model=list[schemes.Client])
def get_all_clients(db: Session = Depends(get_db)):
    return get_clients(db)


@router.post("/create", response_model=schemes.Client)
def add_the_client(name: str, db: Session = Depends(get_db)):
    return add_client(db, name)


@router.delete("", response_model=schemes.Client)
def delete_the_client(client_id: int, db: Session = Depends(get_db)):
    return delete_client(db=db, client_id=client_id)