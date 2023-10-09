import os

from pydantic import Field
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

# Will read in environment variable passed through Docker and validate that it's a postfreszl link
class Settings(BaseSettings):
    database_url: PostgresDsn

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings

# Define settings class
# BaseSettings from pydantic validates the data on creation of instance
# Auto loads db url from environment variable