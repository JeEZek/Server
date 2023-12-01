from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.users import get_users, add_user, update_user, delete_user
from database.database import get_db
from schemes import schemes

router = APIRouter()


@router.get("/{client_id}", response_model=list[schemes.User])
def get_users_from_the_client(client_id: int, db: Session = Depends(get_db)):
    return get_users(db, client_id)


@router.put("/{client_id}", response_model=schemes.User)
def add_user_to_the_client(client_id: int, name: str, address: str, email: str, db: Session = Depends(get_db)):
    return add_user(db=db, name=name, address=address, email=email, owner_id=client_id)


@router.put("/{client_id}/{user_id}", response_model=schemes.User)
def update_the_user(client_id: int, user_id, name: str = None, address: str = None, email: str = None,
                    db: Session = Depends(get_db)):
    return update_user(db=db, owner_id=client_id, user_id=user_id, name=name, address=address, email=email)


@router.delete("/delete.", response_model=schemes.User)
def delete_user_from_the_client(owner_id: int, user_id: int, db: Session = Depends(get_db)):
    return delete_user(owner_id=owner_id, user_id=user_id, db=db)
