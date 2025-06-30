from sqlmodel import Field, Session, SQLModel, create_engine, Relationship
from typing import List, Optional

class Item(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str 
    price: int 
    is_offer: bool 
    user_id: int = Field(foreign_key="user.id")

    creator: Optional["User"] = Relationship(back_populates="items")

class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str 
    email: str
    password: str

    items: list[Item] = Relationship(back_populates="creator")
