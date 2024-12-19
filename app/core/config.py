from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    API_KEY: str
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHANNEL_ID: str
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    PROJECT_NAME: str = "Telegram Relay API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
