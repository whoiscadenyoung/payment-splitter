import os
from typing import Annotated

from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .db.database import SessionLocal

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "5ba39c8dcf037e019590c74917dff6adc05e380bad970b10bb1660bc1fc13450"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Pydantic model will be token endpoint for reponse
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create instance of the clas, pass in token as an argument
# Frontend will use this url to send a username and password, return a token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    """Dependency to create DB sessions to read/write"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_password_hash(password: str):
    """ Will hash the user's password so it can be added to the database """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """ Verify the password entered against the hashed password in the database """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    """ Create a JWT token and return it to the browser """
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Receives a token and returns the user associated with that token
# Decode the token, verify it, and return the current user based on it
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """ Receives a token, decodes and verifies it, returns associated user """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
