# Import FastAPI factory class to create instance for the app, used by uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import libraries for query validation
from typing import Annotated
from fastapi import Body, Path, Query

# Import pydantic to create data models for request body and response
from pydantic import BaseModel, Field

# Create enums to have a fixed set of possible path parameter values
from enum import Enum


class ModelName(str, Enum): 
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Use fields with basemodels to add validation to models (ex: for posting data)
class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, title="Description of item", max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    # Can define subtypes such as Python lists or another class; type annotations only included by default with 3.10+
    tags: set[str] = set()

class Item2(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str | None = None


fake_items_db = [{"item_name": "Foasdofs"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


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
# If using Python 3.6, import Union to accomplish optional query parameters
# bool can be 1, True, true, on, yes, etc.
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


# Declare more validations and metadata for path paramaters (instead of queries) using Path
# Use gt, ge, lt, le to define number ranges (greather than, greater or equal to, etc.)
@app.get("/items2/{item_id}")
async def read_items2(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=1000)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Can get query parameters with ?skip=0&limit=10
# Passed as strings but are converted and validated when processing
# Define limit as entirely optional (no default) with limit: int | None = None
# Annotated is part of standard Pythong typing library, adds metadata to parameters
# Value is optional if = None and required if no default or if = ... (ellipsis)
# Can also require uers to declare None as a value with Annotated[str | None, Query()] = ...
@app.get("/items/")
async def read_items(
    skip: int = 0, 
    limit: int = 10, 
    q: Annotated[
        str | None, 
        Query(
            # 
            title="query string",
            description="query string for the items to search in the database",
            # Set aliases if you have a name to use that's not pythonically valid
            alias="item-query",
            min_length = 3, 
            max_length=50, 
            # Can even specify regex w/ the query pattern option
            pattern = "^fixedquery$",
            # Set deprecated to discourage use before completely getting rid of it
            decrecated=True,
            # Hide query from docs by setting this to false
            include_in_schema=True,
        )
    ] = None):
    """[summary]
    Gets all items. 

    [description]
    Endpoint for all items
    """
    results = {"items": fake_items_db[skip : skip + limit]}
    if q:
        results.update({"q": q})
    return results

# Allows you to declare query multiple times in url /?q=foo&q=bar
@app.get("/items2/")
async def read_items2(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"})
    return item


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

####################################################################################################
# Post Requests
####################################################################################################

# Declares a JSON object that can be passed in the request body. Description and tax are optional in the dict
# Will auto read body, convert types, validate data, return Item, generate JSON schema for docs

# Can combine path parameters and function parameters into one route
# single type parameters (str, int, etc) are interpreted as query parameters
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# Use pydantic models in request
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


# Can put multiple body parameters in a single request, will generate the JSON schema
@app.put("/useritems/{item_id}")
async def update_item(
    item_id: int, 
    # Use embed = true to require nested response with item as key and value as the dict of item elements
    item: Annotated[Item, Body(embed=True)], 
    # Add another body parameter using Body and it will treat it as a parent body key
    user: User, importance: Annotated[int, Body(gt=0)], q: str | None = None):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


@app.post("/items/")
async def create_item(item: Item):
    """[summary]
    Creates an item.

    [description]
    Endpoint for creating an item
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

