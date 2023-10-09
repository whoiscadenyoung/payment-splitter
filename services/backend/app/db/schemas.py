""" Schemas to receive data from database """
from pydantic import BaseModel

class GroupBase(BaseModel):
    """ Base group model """
    name: str
    description: str | None = None


class GroupCreate(GroupBase):
    """ Model for group creation. Pass = no additional fields from Base """
    pass


class GroupModel(GroupBase):
    """ Model for reading group from database """
    id: int
    owner_id: int

    class Config:
        """ Set up configuration to read from database"""
        from_attributes = True


class UserBase(BaseModel):
    """ Base user model """
    email: str
    username: str


class UserCreate(UserBase):
    """ Write user to database """
    email: str
    username: str
    given_name: str
    family_name: str
    password: str
    confirm_password: str


class UserLogin(BaseModel):
    """ Receive login info to authenticate user"""
    email: str
    password: str


class UserReset(BaseModel):
    """ Receive reset info to reset user password"""
    email: str
    password: str
    confirm_password: str


class UserModel(UserBase):
    """ Read user from database--doesn't contain password """
    id: int
    given_name: str
    family_name: str
    is_active: bool
    groups: list[GroupModel] = []

    class Config:
        """ Configure to read as properties from database """
        from_attributes = True

