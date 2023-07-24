from fastapi import FastAPI
from objects import User
from db_layer.db import get_db_object, verify_user_unique


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Punch Me!"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    db = get_db_object()
    user_info = db.read_item(item=user_id, partition_key=user_id)
    return user_info

@app.post("/users/")
async def create_user(user: User):
    # verify a user is unique
    verify_user_unique(user)
    
    client = get_db_object()

    # TODO: Need a better way to create user object
    new_user = dict(user)
    new_user["id"] = user.user_id
    new_user["userid"] = user.user_id
    client.create_item(body=new_user)
    return new_user


@app.get("/punches/{punch_id}")
async def get_punch(punch_id: int):
    return {"punch_id": punch_id}


@app.get("/punch-items/{punch_item_id}")
async def get_punch_item(punch_item_id: int):
    return {"punch_item_id": punch_item_id}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


