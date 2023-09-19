import os

from pydantic import BaseSettings, Field


# Define settings class
# BaseSettings from pydantic validates the data on creation of instance
# Auto loads db url from environment variable
class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')

settings = Settings()