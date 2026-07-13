from fastapi import APIRouter,Depends
from routers.schemas import UserBase,UserDisplay
from database.database import get_db
from sqlalchemy.orm.session import Session
from database import db_user

router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post('', response_model= UserDisplay)
def create_user(request:UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(db, request)