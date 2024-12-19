import httpx
from typing import Dict, Any
from app.core.config import get_settings

settings = get_settings()


class TelegramService:
    def __init__(self):
        self.bot_token = settings.TELEGRAM_BOT_TOKEN
        self.channel_id = settings.TELEGRAM_CHANNEL_ID
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

    async def send_message(self, message: str) -> Dict[str, Any]:
        """Send message to Telegram channel"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/sendMessage",
                params={
                    "chat_id": self.channel_id,
                    "text": message,
                    "parse_mode": "HTML",
                },
            )
            response.raise_for_status()
            return response.json()

    async def send_photo(self, photo_url: str, caption: str = "") -> Dict[str, Any]:
        """Send photo to Telegram channel"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/sendPhoto",
                params={
                    "chat_id": self.channel_id,
                    "photo": photo_url,
                    "caption": caption,
                    "parse_mode": "HTML",
                },
            )
            response.raise_for_status()
            return response.json()
