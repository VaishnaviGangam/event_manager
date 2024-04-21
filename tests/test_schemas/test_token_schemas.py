import pytest
from app.schemas.token_schemas import Token, TokenData, RefreshTokenRequest

# Token Models Test Cases
@pytest.fixture
def example_access_token():
    return "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

@pytest.fixture
def example_username():
    return "user@example.com"

@pytest.fixture
def refresh_token():
    return "refresh_token_here"

def test_token_model_example(example_access_token):
    token = Token(access_token=example_access_token)
    assert token.access_token == example_access_token
    assert token.token_type == "bearer"

def test_token_data_model_example(example_username):
    token_data = TokenData(username=example_username)
    assert token_data.username == example_username

def test_refresh_token_request_model(refresh_token):
    refresh_request = RefreshTokenRequest(refresh_token=refresh_token)
    assert refresh_request.refresh_token == refresh_token
