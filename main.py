from fastapi import FastAPI
from database import models
from database.database import engine
from routers import user
from routers import post
from auth import authentication
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)

@app.get('/')
def home():
    return "Hello , this is root"

models.Base.metadata.create_all(engine)
app.mount('/images', StaticFiles(directory='images'), name='images')