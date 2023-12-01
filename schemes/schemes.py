from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    name: str
    address: str
    email: str


class User(UserBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class ClientBase(BaseModel):
    name: str


class Client(ClientBase):
    id: int
    users: List[User] = []

    class Config:
        from_attributes = True
