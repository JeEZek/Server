from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from models import models
from models.models import Client


def get_clients(db: Session):
    return db.query(models.Client).all()


def add_client(db: Session, name: str):
    new_client = Client(name=name)
    if new_client:
        return JSONResponse(content={"message": "Client with this name already exists"})

    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return JSONResponse(content={"message": "Client created successfully"})


def delete_client(db: Session, client_id: int):
    db_client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    db.query(models.User).filter(models.User.owner_id == client_id).delete()
    db.delete(db_client)
    db.commit()

    return JSONResponse(content={"message": "Client and associated users deleted successfully"})


