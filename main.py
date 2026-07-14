from fastapi import FastAPI
from database import models
from database.database import engine
from routers import user
from routers import post
from auth import authentication
from routers import comment
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(comment.router)

@app.get('/')
def home():
    return "Hello , this is root"


models.Base.metadata.create_all(engine)
app.mount('/images', StaticFiles(directory='images'), name='images')

origins = [
    "http://locahost:port#"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers= "*"
)