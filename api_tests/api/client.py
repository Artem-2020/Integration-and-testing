import requests
from typing import Dict, Any, Optional

class MealDBClient:
    BASE_URL = "https://www.themealdb.com/api/json/v1/1"

    def __init__(self, timeout: int = 10):
        self.session = requests.Session()
        self.timeout = timeout
        self.session.headers.update({
            "User-Agent": "MealDB-Testing/1.0"
        })

    def _request(self, method: str, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def search_by_name(self, meal_name: str) -> Dict:
        """Поиск блюда по названию."""
        return self._request("GET", "search.php", params={"s": meal_name})

    def get_random_meal(self) -> Dict:
        """Получение случайного блюда."""
        return self._request("GET", "random.php")