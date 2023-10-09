""" Routes for authentication"""
from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils import get_db, create_access_token, Token
from app.db import crud, schemas
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/reset/", response_model=schemas.UserModel)
def reset_user(user_reset: schemas.UserReset, db: Session = Depends(get_db)):
    """ Route to send user password reset request to update database """
    if not user_reset.password == user_reset.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    user = crud.reset_user_password(db, email=user_reset.email, password=user_reset.password)
    if not user:
        raise HTTPException(status_code=400, detail="Cannot reset password")
    return user


# Path to create a jwt token and return it
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
    ):
    """
    Login/token: Pass in OAuth2PasswordRequestForm with username and password. 
    Return with access token after validating in the database
    """
    user = crud.authenticate_user_by_email(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
