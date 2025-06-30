from fastapi import APIRouter, status, HTTPException
import schemas
from database import SessionDep
import model
from hashing import get_password_hash

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.post("/", response_model=schemas.User)
def create_user(request: schemas.User, session: SessionDep):
    new_user = model.User(name=request.name, email=request.email, password=get_password_hash(request.password))
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id:int, session: SessionDep):
    user = session.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
