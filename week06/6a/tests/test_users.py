import requests

def test_valid_credentials():
    """
    Test 1: Call the endpoint with valid credentials and expect HTTP 200.
    """
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"
    response = requests.get(url)
    assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"

def test_invalid_credentials():
    """
    Test 2: Call the endpoint with invalid credentials and expect HTTP 401.
    """
    url = "http://127.0.0.1:8000/users/?username=admin&password=admin"
    response = requests.get(url)
    assert response.status_code == 401, f"Expected HTTP 401, got {response.status_code}"
