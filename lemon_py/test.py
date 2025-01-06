import requests
import pytest

# Base URL for the login API
BASE_URL = "https://dummyjson.com/auth/login"

# Define test fixtures for valid and invalid payloads
@pytest.fixture
def valid_payload():
    """
    Returns a valid payload with correct username and password.
    """
    return {"username": "emilys", "password": "emilyspass"}

@pytest.fixture
def invalid_payload():
    """
    Returns an invalid payload with incorrect username and password.
    """
    return {"username": "invaliduser", "password": "wrongpassword"}

# Test case for login with valid credentials
def test_login_api_valid_credentials(valid_payload):
    """
    Test the login API with valid credentials.
    - Sends a POST request with valid credentials.
    - Asserts that the response status code is 200.
    - Asserts that an access token is present in the response.
    """
    response = requests.post(BASE_URL, json=valid_payload)

    assert response.status_code == 200, "Expected status code 200 for valid credentials"

    assert "accessToken" in response.json(), "Token not found in the response for valid credentials"

# Test case for login with invalid credentials
def test_login_api_invalid_credentials(invalid_payload):
    """
    Test the login API with invalid credentials.
    - Sends a POST request with invalid credentials.
    - Asserts that the response status code is 400.
    - Asserts that the error message matches "Invalid credentials".
    """
    response = requests.post(BASE_URL, json=invalid_payload)

    # Print the error message from the response for debugging purposes
    print(response.json()["message"])

    assert response.status_code == 400, "Expected status code 400 for invalid credentials"
    assert response.json()["message"] == "Invalid credentials", "Expected error message for invalid credentials"
