import requests


def login(base_url: str, username: str, password: str) -> requests.Session:
    """
    Authenticate against the MDM application and return an authenticated session.

    Args:
        base_url: Base URL of the MDM application (e.g. 'https://mdm.example.com')
        username: Login username
        password: Login password

    Returns:
        Authenticated requests.Session

    Raises:
        ValueError: If login fails due to invalid credentials
        requests.HTTPError: If the server returns an unexpected HTTP error
    """
    session = requests.Session()
    login_url = f"{base_url.rstrip('/')}/login"

    payload = {
        "username": username,
        "password": password,
    }

    response = session.post(login_url, data=payload)
    response.raise_for_status()

    if "invalid" in response.text.lower() or "incorrect" in response.text.lower():
        raise ValueError("Login failed: invalid username or password")

    return session
