from routers.schemas import PostBase,PostDisplay
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from database.models import DbPost
from datetime import datetime

def createpost(db:Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db:Session):
    return db.query(DbPost).all()

def delete(db:Session, id:int, user_id :int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user not found with id {id}")
    if not post.user_id == user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="ony the user who created post can delete it")
    
    db.delete(post)
    db.commit
    return "ok"