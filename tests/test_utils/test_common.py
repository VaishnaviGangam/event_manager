import pytest
from datetime import datetime, timedelta
from app.utils.common import authenticate_user, create_access_token, validate_and_sanitize_url, verify_refresh_token
from app.dependencies import get_settings
from fastapi import HTTPException, status

settings = get_settings()

@pytest.mark.parametrize("username, password, expected", [
    ("admin", "secret", {"username": "admin"}),  # Valid credentials
    ("user", "wrongpassword", None),  # Invalid credentials
])
def test_authenticate_user(username, password, expected):
    result = authenticate_user(username, password)
    assert result == expected

@pytest.mark.parametrize("data, expires_delta", [
    ({"sub": "user"}, timedelta(minutes=15)),  # Valid data and expiration time
    ({"sub": "admin"}, timedelta(hours=1)),    # Valid data and expiration time
])
def test_create_access_token(data, expires_delta):
    # Act
    token = create_access_token(data, expires_delta)
    # Assert
    assert isinstance(token, str) and token != ""  # Ensure a non-empty string is returned

@pytest.mark.parametrize("url_str, expected", [
    ("http://example.com", "http://example.com"),  # Valid URL
    ("invalid_url", None),                         # Invalid URL
])
def test_validate_and_sanitize_url(url_str, expected):
    # Act
    result = validate_and_sanitize_url(url_str)
    # Assert
    assert result == expected

@pytest.mark.parametrize("refresh_token, expected", [
    (create_access_token({"sub": "user"}, timedelta(minutes=30)), {"username": "user"}),  # Valid refresh token
    (create_access_token({"sub2": "user"}, timedelta(minutes=30)), status.HTTP_401_UNAUTHORIZED),  # Invalid token
])
def test_verify_refresh_token(refresh_token, expected):
    # Act
    if isinstance(expected, dict):
        result = verify_refresh_token(refresh_token)
        # Assert
        assert result == expected
    else:
        with pytest.raises(HTTPException) as exc_info:
            verify_refresh_token(refresh_token)
        assert exc_info.value.status_code == expected
