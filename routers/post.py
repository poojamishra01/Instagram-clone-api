from fastapi import APIRouter,Depends, HTTPException, status, UploadFile,File
from typing import List
from sqlalchemy.orm.session import Session
from database.database import get_db
from routers.schemas import PostBase, PostDisplay, UserAuth
from database import db_post
import random
import string
import shutil
from auth.oauth2 import get_current_user

router= APIRouter(
    prefix="/post",
    tags=['post']
)

image_url_types = ['absolute', 'relative']

@router.post('',response_model=PostDisplay)
def create(request:PostBase, db:Session = Depends(get_db), current_user:UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="parameter image_url_type can only be absolute or relative")
    
    return db_post.createpost(db,request)    

@router.get('/all', response_model=List[PostDisplay])
def get_all_post(db:Session= Depends(get_db)):
    return db_post.get_all(db)


@router.post('/images')
def upload_image(image:UploadFile= File(...),current_user:UserAuth = Depends(get_current_user)):
    letters= string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'

    filename = new.join(image.filename.rsplit('.',1))

    path = f'images/{filename}'
    with open(path,'w+b') as buffer:
        shutil.copyfileobj(image.file,buffer)

    return {
        'filename':path
    }

@router.get('/delete/{id}')
def delete_post(id: int, db:Session= Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete(db, id, current_user.id)
