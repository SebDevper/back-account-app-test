from typing import Annotated, Union
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from api_controllers.create_user import create_new_user
from api_controllers.login import login
from api_controllers.accounts import get_accounts
from api_controllers.banks import get_all_banks_from_api
from api_controllers.accounts import get_accounts_by_bank_from_api
from api_controllers.transactions import get_transactions_by_account_from_api
from models.user import User
from models.userlogin import UserLogin
from db_actions.token import get_token
import os

app = FastAPI()

origins = [
    "http://127.0.0.1:8080",
    "https://front-account-test-project-5u6m.vercel.app",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/get_all_banks/")
def get_all_banks(token: Annotated[str | None, Header()] = None):
    if not get_token(token):
        return {'error': 'no auth'}
    return get_all_banks_from_api()

@app.get("/get_bank_accounts/{bank_code}")
def get_accounts_by_bank(bank_code: str, token: Annotated[str | None, Header()] = None):
    if not get_token(token):
        return {'error': 'no auth'}
    return get_accounts_by_bank_from_api(bank_code)

@app.get("/get_account_transactions/{account_id}/{link_id}")
def get_accounts_by_bank(account_id: str, link_id: str, token: Annotated[str | None, Header()] = None):
    if not get_token(token):
        return {'error': 'no auth'}
    return get_transactions_by_account_from_api(account_id, link_id)
