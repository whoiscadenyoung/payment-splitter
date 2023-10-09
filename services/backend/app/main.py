""" Main module of FastaAPI backend """
from typing import Annotated

import time

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db import crud, models, schemas
from app.db.database import engine
from app.utils import oauth2_scheme, verify_password, get_db, get_current_user
from app import routers

# Bind models to engine and create it
models.Base.metadata.create_all(bind=engine)

# instantiate the FastAPI app
# access docs with /docs or /redoc
# Possible next + fastapi: https://github.com/digitros/nextjs-fastapi
app = FastAPI()

# CORS: for production make sure allow_origins only allows the frontend of http://localhost:8080
origins = ["http://localhost:3000", "http://payment-frontend:3000"]
app.add_middleware(CORSMiddleware, 
    allow_origins=origins, 
    allow_methods=["*"], 
    allow_headers=["*"], 
    expose_headers=["*"], 
    allow_credentials=True,)

app.include_router(routers.auth.router)
app.include_router(routers.users.router)
app.include_router(routers.groups.router)

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


@app.get("/users/me")
async def read_users_me(current_user: Annotated[schemas.UserModel, Depends(get_current_user)]):
    return current_user


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/users/", response_model=schemas.UserModel)
# SQLAlchemy doesn't have support for db_user = await so these must be declared as def
def create_user(token: Annotated[str, Depends(oauth2_scheme)], user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login")
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Incorrect email or password")
    if not verify_password(plain_password=user.password, hashed_password=db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    encoded_jwt = jwt.encode
    return {"message": "Login successful"}


@app.get("/users/", response_model=list[schemas.UserModel])
# Add a token here dependent on oauth2; dependency provides a string assigned to parameter token of path operation function
# Will look for authorization header, check if has Bearer token, return token as str
# Will return 401 unauthorized directly if no token
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserModel)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users/{user_id}/groups/", response_model=schemas.GroupModel)
def create_group_for_user(user_id: int, group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create_user_group(db=db, group=group, user_id=user_id)


@app.get("/groups/", response_model=list[schemas.GroupModel])
def read_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups