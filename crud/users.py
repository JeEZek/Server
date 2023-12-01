from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from pydantic import EmailStr

from models import models


def get_users(db: Session, owner_id: int):
    return db.query(models.User).join(models.Client).filter(models.Client.id == owner_id).all()


def add_user(db: Session, name: str, address: str, email: EmailStr, owner_id: int):
    db_client = db.query(models.Client).filter(models.Client.id == owner_id).first()
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    db_user = models.User(name=name, address=address, email=email, owner_id=owner_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return JSONResponse(content={"message": "User added successfully"})


def update_user(db: Session, name: str, address: str, email: EmailStr, owner_id: int, user_id: int):
    db_user = db.query(models.User).filter(
        models.User.id == user_id, models.User.owner_id == owner_id
    ).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        db_user.name = name
    if address is not None:
        db_user.address = address
    if email is not None:
        db_user.email = email

    db.commit()

    return JSONResponse(content={"message": "User updated successfully"})


def delete_user(owner_id: int, user_id: int, db: Session):
    db_client = db.query(models.Client).filter(models.Client.id == owner_id).first()

    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")

    db_user = db.query(models.User).filter(
        models.User.id == user_id, models.User.owner_id == owner_id
    ).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return JSONResponse(content={"message": "User deleted successfully"})
