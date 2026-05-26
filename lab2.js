// Пример для сценария API-TMDB-01 и API-TMDB-02 (Успешный поиск и проверка структуры)

// 1. Проверка кода состояния
pm.test("Status code is 200 OK", function () {
    pm.response.to.have.status(200);
});

// 2. Проверка времени ответа
pm.test("Response time is less than 2000ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(2000);
});

// 3. Проверка заголовка Content-Type
pm.test("Content-Type header is present", function () {
    pm.response.to.have.header("Content-Type");
});

// 4. Проверка тела ответа (что meals не null и содержит данные)
pm.test("Response has meals and it is not null", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.meals).to.not.be.null;
    pm.expect(responseJson.meals).to.be.an('array').that.is.not.empty;
});

// 5. Проверка структуры первого рецепта в массиве
pm.test("First meal has required fields (id, name, instructions, thumb)", function () {
    const responseJson = pm.response.json();
    const firstMeal = responseJson.meals[0];
    
    pm.expect(firstMeal).to.have.property('idMeal');
    pm.expect(firstMeal.idMeal).to.be.a('string').and.to.have.lengthOf.at.least(1);
    
    pm.expect(firstMeal).to.have.property('strMeal');
    pm.expect(firstMeal.strMeal).to.be.a('string').and.to.not.be.empty;
    
    pm.expect(firstMeal).to.have.property('strInstructions');
    pm.expect(firstMeal.strInstructions).to.be.a('string').and.to.not.be.empty;
    
    pm.expect(firstMeal).to.have.property('strMealThumb');
    pm.expect(firstMeal.strMealThumb).to.be.a('string').and.to.match(/^https?:\/\/.+/); // Проверка, что это URL
});