from pydantic import BaseModel
from typing import List

class ItemBase(BaseModel):
    name: str
    price: int
    is_offer: bool = None


class Item(ItemBase):

    class Config():
        from_attributes = True


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    items: List[Item]


class ShowItem(BaseModel):
    name: str
    price: int
    is_offer: bool = None
    # creator: ShowUser

    # class Config():
    #     from_attributes = True