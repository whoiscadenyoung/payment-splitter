""" Database initialization """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

# Create the engine
# If using SQLite, add arg: connect_args = {"check_same_thread": False}
engine = create_engine(str(get_settings().database_url))

# Create a SessionLocal class that can be used to instantiate a database session later on
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
