from pydantic import BaseModel
from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    API_KEY: str = os.getenv("API_KEY")
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID: str = os.getenv("TELEGRAM_CHANNEL_ID")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    PROJECT_NAME: str = "Telegram Relay API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    class Config:
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
