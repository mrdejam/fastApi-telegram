import pytest
from app.core.config import get_settings

settings = get_settings()


def test_send_message_without_api_key(client):
    response = client.post(
        f"{settings.API_V1_STR}/messages/send", json={"message": "Test message"}
    )
    assert response.status_code == 403


def test_send_message_with_invalid_api_key(client):
    response = client.post(
        f"{settings.API_V1_STR}/messages/send",
        headers={"X-API-Key": "invalid_key"},
        json={"message": "Test message"},
    )
    assert response.status_code == 403


def test_send_message_without_content(client):
    response = client.post(
        f"{settings.API_V1_STR}/messages/send",
        headers={"X-API-Key": settings.API_KEY},
        json={},
    )
    assert response.status_code == 422
