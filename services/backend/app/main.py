from typing import Union

# Import FastAPI factory class to create instance for the app, used by uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create enums to have a fixed set of possible path parameter values
from enum import Enum


class ModelName(str, Enum): 
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


fake_items_db = [{"item_name": "Foofs"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# instantiate the FastAPI app
# access docs with /docs or /redoc
app = FastAPI()

# CORS: for production make sure allow_origins only allows the frontend of http://localhost:8080
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


# declare path parameters/variables like Python format strings; arg is passed into function
# parameters not defined in path are query parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    """[summary]
    Gets all items. 

    [description]
    Endpoint for all items
    """
    return fake_items_db[skip : skip + limit]


# Paths are evaluated in order with more specific ones going before the general catch-alls
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Path for models defined in enum
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """[summary]
    Gets a model by name.

    [description]
    Endpoint for a model
    """
    if model_name is ModelName.alexnet:
        # You can return enums directly and they will be converted to strings/values
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    elif model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


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