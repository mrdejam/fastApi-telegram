from fastapi import APIRouter, Depends, HTTPException
import httpx
from pydantic import BaseModel
from typing import Optional
from app.core.security import verify_api_key
from app.services.telegram import TelegramService

router = APIRouter()
telegram_service = TelegramService()


class MessageRequest(BaseModel):
    message: str
    photo_url: Optional[str] = None


@router.post("/send")
async def send_message(request: MessageRequest, api_key: str = Depends(verify_api_key)):
    """
    Send a message to the Telegram channel
    """
    try:
        if request.photo_url:
            result = await telegram_service.send_photo(
                photo_url=request.photo_url, caption=request.message
            )
        else:
            result = await telegram_service.send_message(request.message)

        return {
            "status": "success",
            "message": "Content sent to Telegram channel",
            "telegram_response": result,
        }

    except httpx.HTTPError as e:
        error_message = str(e)
        if "404" in error_message:
            detail = "Invalid photo URL: Image not found"
        elif "400" in error_message:
            detail = (
                "Invalid request: Please check your photo URL is accessible and valid"
            )
        else:
            detail = f"Telegram API error: {error_message}"

        raise HTTPException(status_code=400, detail=detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
