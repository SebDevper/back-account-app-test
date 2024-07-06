from typing import Annotated, Union
from fastapi import FastAPI, Header
from api_controllers.create_user import create_new_user
from api_controllers.login import login
from api_controllers.accounts import get_accounts
from models.user import User
from models.userlogin import UserLogin
from db_actions.token import get_token
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


@app.post("/login/")
def login_user(user_login: UserLogin):
    return login(user_login)

@app.get("/get_accounts_by_bank/")
def get_bank_list(token: Annotated[str | None, Header()] = None):
    if not get_token(token):
        return {'error': 'no auth'}

    return get_accounts()
