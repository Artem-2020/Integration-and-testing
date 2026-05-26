import pytest
from api.schemas import SearchResponse, Meal

class TestMealDB:
    """Тесты для TheMealDB API."""

    @pytest.mark.positive
    def test_search_existing_meal(self, api_client, known_meal):
        """Поиск существующего блюда возвращает корректные данные."""
        response = api_client.search_by_name(known_meal)
        # Проверяем, что ответ не пустой
        assert response["meals"] is not None, "Ответ не должен быть пустым"

        # Валидация структуры через Pydantic
        search_response = SearchResponse(**response)
        assert len(search_response.meals) > 0, "Список блюд не должен быть пуст"
        first_meal = search_response.meals[0]

        # Проверяем, что название содержит искомое слово (регистронезависимо)
        assert known_meal.lower() in first_meal.strMeal.lower(), \
            f"Название блюда '{first_meal.strMeal}' не содержит '{known_meal}'"
        assert first_meal.idMeal is not None, "ID блюда отсутствует"

    @pytest.mark.negative
    def test_search_non_existing_meal(self, api_client, unknown_meal):
        """Поиск несуществующего блюда возвращает пустой ответ (meals = null)."""
        response = api_client.search_by_name(unknown_meal)
        # Согласно документации, при отсутствии результатов API возвращает {"meals": null}
        assert response["meals"] is None, "Должен вернуться null для несуществующего блюда"

    @pytest.mark.positive
    def test_random_meal_returns_one(self, api_client):
        """Случайное блюдо возвращает ровно один результат."""
        response = api_client.get_random_meal()
        assert response["meals"] is not None, "Ответ не должен быть пустым"
        meals = response["meals"]
        assert len(meals) == 1, "Должно вернуться ровно одно блюдо"
        meal = Meal(**meals[0])   # валидируем структуру через Pydantic
        assert meal.idMeal, "ID блюда отсутствует"
        assert meal.strMeal, "Название блюда отсутствует"