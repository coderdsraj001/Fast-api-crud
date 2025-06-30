from fastapi import APIRouter, status, HTTPException
from typing import List
import schemas
from database import SessionDep
import model

router = APIRouter(
    prefix="/item",
    tags=["items"]
)


@router.get("/", response_model=List[schemas.Item])
def all_item(session: SessionDep):
    items = session.query(model.Item).all()
    return items

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(request: schemas.Item, session: SessionDep):
    new_item = model.Item(name=request.name, price=request.price, is_offer= request.is_offer, user_id=1)
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    return {"data": new_item}

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowItem)
def show(id, session: SessionDep):
    item = session.query(model.Item).filter(model.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Item, session: SessionDep):
    item = session.query(model.Item).filter(model.Item.id == id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    item_dict = request.dict(exclude_unset=True)
    item.update(item_dict)
    session.commit()
    return "updated"


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id, session: SessionDep):
    item = session.query(model.Item).filter(model.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    session.delete(item)
    session.commit()
    return item