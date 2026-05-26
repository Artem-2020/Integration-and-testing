from __future__ import annotations

import allure

from pages.main_page import MainPage


@allure.epic("Лабораторная работа №6")
@allure.feature("Навигация в приложении NewPipe")
class TestNewPipeNavigation:
    @allure.title("TC-01. Переход в Settings через navigation drawer")
    def test_open_settings_from_navigation_drawer(self, driver):
        main_page = MainPage(driver)

        with allure.step("Проверить, что главное окно приложения открыто"):
            assert main_page.is_loaded(), "Главный экран NewPipe не загрузился"
            main_page.attach_screenshot("01_main_screen")

        with allure.step("Открыть drawer и перейти в Settings"):
            main_page.open_drawer()
            settings_page = main_page.open_settings()

        with allure.step("Проверить состав основных разделов настроек"):
            assert settings_page.is_loaded(), "Экран настроек не открылся"
            assert settings_page.has_core_categories(), (
                "На экране настроек отсутствуют ожидаемые категории"
            )
            settings_page.attach_screenshot("02_settings_screen")

    @allure.title("TC-02. Переход в About & FAQ через navigation drawer")
    def test_open_about_screen_from_navigation_drawer(self, driver):
        main_page = MainPage(driver)

        with allure.step("Проверить доступность главного экрана"):
            assert main_page.is_loaded(), "Главный экран NewPipe не загрузился"

        with allure.step("Открыть drawer и перейти в About & FAQ"):
            main_page.open_drawer()
            about_page = main_page.open_about()

        with allure.step("Проверить вкладки About & FAQ и Licenses, а также версию приложения"):
            assert about_page.is_loaded(), "Экран About не открылся"
            assert about_page.has_expected_content(), (
                "На экране About отсутствуют ожидаемые элементы"
            )
            about_page.attach_screenshot("03_about_screen")
