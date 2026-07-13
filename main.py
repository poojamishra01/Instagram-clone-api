from fastapi import FastAPI
from database import models
from database.database import engine

app = FastAPI()

@app.get('/')
def home():
    return "Hello , this is root"

models.Base.metadata.create_all(engine)