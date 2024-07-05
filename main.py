from typing import Union
from fastapi import FastAPI
from api_controllers.create_user import create_new_user
from models.user import User
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"Item_ID": item_id, "q": q}

@app.post("/create-user/")
def create_user(user: User): 
    return create_new_user(user)
