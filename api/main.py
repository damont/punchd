from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Punch Me!"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/punches/{punch_id}")
async def get_punch(punch_id: int):
    return {"punch_id": punch_id}


@app.get("/punch-items/{punch_item_id}")
async def get_punch_item(punch_item_id: int):
    return {"punch_item_id": punch_item_id}


@app.get("/itmes/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}


