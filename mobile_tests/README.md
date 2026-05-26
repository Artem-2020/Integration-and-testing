# NewPipe Appium Tests

Проект подготовлен для лабораторной работы №6 по автоматизации мобильного тестирования с использованием `Appium + Python + pytest + Allure`.

## Что автоматизировано

- `TC-01` Переход в `Settings` через navigation drawer и проверка основных категорий настроек.
- `TC-02` Переход в `About & FAQ` через navigation drawer и проверка вкладок `About & FAQ`, `Licenses`, а также версии приложения.

## Подтвержденные данные приложения

- Приложение: `NewPipe`
- Пакет: `org.schabi.newpipe`
- Главная activity: `org.schabi.newpipe.MainActivity`
- Экран настроек: `org.schabi.newpipe.settings.SettingsActivity`
- Экран About: `org.schabi.newpipe.about.AboutActivity`
- Последний релиз, использованный для конфигурации: `v0.28.7`
- APK: `NewPipe_v0.28.7.apk`

## Рекомендуемая структура

```text
mobile_tests/
├── artifacts/
│   └── screenshots/
├── pages/
├── tests/
├── utils/
├── conftest.py
├── config.py
├── pytest.ini
└── requirements.txt
```

## Подготовка окружения

1. Установить Python-зависимости:

```powershell
pip install -r requirements.txt
```

2. Положить `NewPipe_v0.28.7.apk` в каталог:

```text
mobile_tests/artifacts/NewPipe_v0.28.7.apk
```

3. Запустить Appium Server:

```powershell
appium
```

4. Убедиться, что эмулятор или устройство доступны через `adb devices`.

## Переменные окружения

По умолчанию проект ожидает:

- `APPIUM_SERVER_URL=http://127.0.0.1:4723`
- `DEVICE_NAME=Android Emulator`
- `APP_LANGUAGE=en`
- `APP_LOCALE=US`
- `APP_PACKAGE=org.schabi.newpipe`
- `MAIN_ACTIVITY=org.schabi.newpipe.MainActivity`
- `APK_PATH=<project>/artifacts/NewPipe_v0.28.7.apk`

При необходимости можно дополнительно задать:

- `UDID`
- `NO_RESET`
- `AUTO_GRANT_PERMISSIONS`
- `NEW_COMMAND_TIMEOUT`

## Запуск тестов

Все тесты:

```powershell
pytest -v
```

С генерацией Allure-результатов:

```powershell
pytest -v --alluredir=reports/allure-results
```

Просмотр Allure-отчёта:

```powershell
allure serve reports/allure-results
```
