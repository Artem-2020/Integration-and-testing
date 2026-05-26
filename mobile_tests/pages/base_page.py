from __future__ import annotations

import re
from pathlib import Path

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import CONFIG

try:
    import allure
except ImportError:  # pragma: no cover
    allure = None


class BasePage:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    @staticmethod
    def text_locator(text: str) -> tuple[str, str]:
        escaped = text.replace('"', '\\"')
        return (
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiSelector().text("{escaped}")',
        )

    def find_element(
        self, locator: tuple[str, str], timeout: int | None = None
    ):
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        return wait.until(EC.visibility_of_element_located(locator))

    def tap(self, locator: tuple[str, str], timeout: int | None = None) -> None:
        wait = WebDriverWait(self.driver, timeout or self.DEFAULT_TIMEOUT)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def is_visible(
        self, locator: tuple[str, str], timeout: int = 5
    ) -> bool:
        try:
            self.find_element(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def wait_for_text(self, text: str, timeout: int = 10) -> None:
        self.find_element(self.text_locator(text), timeout=timeout)

    def take_screenshot(self, name: str) -> Path:
        CONFIG.ensure_directories()
        safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_") or "screen"
        screenshot_path = CONFIG.screenshots_dir / f"{safe_name}.png"
        self.driver.save_screenshot(str(screenshot_path))
        return screenshot_path

    def attach_screenshot(self, name: str) -> Path:
        screenshot_path = self.take_screenshot(name)
        if allure is not None:
            allure.attach.file(
                str(screenshot_path),
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )
        return screenshot_path
