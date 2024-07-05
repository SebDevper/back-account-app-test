from typing import Union
from fastapi import FastAPI
from database import get_connection
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"Item_ID": item_id, "q": q}

@app.get("/create-user/")
def create_user():     
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('select * from user;')

    myresult = cursor.fetchall()    

    print(myresult)

    cursor.close()
    connection.close()

    
    return {'a': myresult}
