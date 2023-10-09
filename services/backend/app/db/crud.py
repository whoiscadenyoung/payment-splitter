""" CRUD operations for interactions with database models """
#  External imports
from sqlalchemy.orm import Session

# Local imports
from app.db import models, schemas
from app.utils import get_password_hash, verify_password

# Functionss here are dedicated only to database interaction, not part of path operation.
# Can be reused this way and you can add unit tests to these too
# Read user by ID and email
def get_user(db: Session, user_id: int):
    """ Get user by ID from database """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """ Get user by email address from database """
    return db.query(models.User).filter(models.User.email == email).first()


# Get multiple users
def get_users(db: Session, skip: int = 0, limit: int = 100):
    """ Get list of all users """
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """ After checking if account already exists, add user and password to db """
    db_user = models.User(email=user.email)
    db_user.hashed_password = get_password_hash(password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_groups(db: Session, skip: int = 0, limit: int = 100):
    """ Get list of all groups """
    return db.query(models.Group).offset(skip).limit(limit).all()


def create_user_group(db: Session, group: schemas.GroupCreate, user_id: int):
    """ Create a group assigned to the specific user """
    # **group.dict() extracts keys from group, puts them directly in the code here
    db_group = models.Group(**group.dict(), owner_id=user_id)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group


def authenticate_user_by_email(db: Session, username: str, password: str):
    """ 
    Takes user email and password, verifies if it matches with database; 
    Returns false or user 
    """
    user = get_user_by_email(db, email=username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def reset_user_password(db: Session, email: str, password: str):
    """ If user account exists for given email, reset the password """
    user = get_user_by_email(db, email=email)
    if not user:
        return False
    user.hashed_password = get_password_hash(password=password)
    db.commit()
    db.refresh(user)
    return user
    
