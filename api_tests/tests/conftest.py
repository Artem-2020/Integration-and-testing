import pytest
from api.client import MealDBClient

@pytest.fixture(scope="session")
def api_client():
    """Фикстура для клиента API."""
    client = MealDBClient()
    yield client

@pytest.fixture
def known_meal():
    """Известное существующее блюдо."""
    return "Arrabiata"

@pytest.fixture
def unknown_meal():
    """Несуществующее блюдо."""
    return "qwertyuiopasdfghjkl"