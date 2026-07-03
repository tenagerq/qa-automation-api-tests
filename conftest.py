import pytest
import requests
@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"
@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    yield session
    session.close()
@pytest.fixture
def new_user_payload():
    return {
        "title": "QA automation",
        "body": "learning pytest",
        "userId": 1
    }