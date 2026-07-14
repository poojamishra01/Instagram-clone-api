from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    username :str
    email:str
    password: str

class UserDisplay(BaseModel):
    id:int
    username:str
    email:str
    class config():
        orm_mode= True

#for postdisplay
class User(BaseModel):
    username:str
    class config():
        orm_mode = True

#for postDisplay
class Comments(BaseModel):
    username:str
    text:str
    timestamp:datetime
    class config():
        orm_mode = True

class PostBase(BaseModel):
    image_url :str
    image_url_type :str
    caption:str
    creator_id: int

class PostDisplay(BaseModel):
    id:int
    image_url:str
    image_url_type:str
    caption:str
    timestamp: datetime
    user :User
    comments : List[Comments]
    class config():
        orm_mode = True

class UserAuth(BaseModel):
    id:int
    username:str
    email:str

class CommentBase(BaseModel):
    username:str
    text:str
    post_id :int




