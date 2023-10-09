""" SQLAlchemy models for the database """
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a Base class that can be used to create models later on
Base = declarative_base()

class User(Base):
    """ User table: per-user information """
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    given_name = Column(String)
    family_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # Create the relationships
    groups = relationship("Group", back_populates="owner")


class Group(Base):
    """ Group table: groups linked to user accounts """
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="groups")
