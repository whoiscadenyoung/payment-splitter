from typing import Union

# Import FastAPI factory class to create instance for the app, used by uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# instantiate the FastAPI app
app = FastAPI()

# CORS: for production make sure allow_origins only allows the frontend of http://localhost:8080
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Paths are evaluated in order with more specific ones going before the general catch-alls
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Path operation decorator for get request: @app.get(route)
# This means function handles requests that go to the /pets/ path using a get operation
@app.get("/pets/")
async def get_all_pets():
    """[summary]
    Gets all pets adopted/rescued or not.

    [description]
    Endpoint for all pets
    """
    fake_pets = [{"name": "Guero", "type": "dog", "adopted": True}, {"name": "Pepita", "type": "cat", "adopted": False}]
    return fake_pets