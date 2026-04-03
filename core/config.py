import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from typing import List

class Settings(BaseSettings):
    ENV: str = "development"
    DATABASE_URL: str = "sqlite:///./finance.db"
    JWT_SECRET_KEY: str = "change_this_secret"
    JWT_REFRESH_SECRET_KEY: str = "change_this_refresh_secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    RATE_LIMIT_LOGIN: int = 5
    RATE_LIMIT_GENERAL: int = 100

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
