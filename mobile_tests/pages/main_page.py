from __future__ import annotations

from appium.webdriver.common.appiumby import AppiumBy

from pages.about_page import AboutPage
from pages.base_page import BasePage
from pages.settings_page import SettingsPage


class MainPage(BasePage):
    DRAWER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Open Drawer")
    SETTINGS_MENU_ITEM = BasePage.text_locator("Settings")
    ABOUT_MENU_ITEM = BasePage.text_locator("About & FAQ")
    KEEP_ANDROID_OPEN_TITLE = BasePage.text_locator("Keep Android Open")
    CHECK_UPDATES_TITLE = BasePage.text_locator("Check for updates")
    DIALOG_OK_BUTTON = BasePage.text_locator("OK")
    DIALOG_NO_BUTTON = BasePage.text_locator("NO")

    def dismiss_startup_dialogs(self) -> None:
        if self.is_visible(self.KEEP_ANDROID_OPEN_TITLE, timeout=5):
            self.tap(self.DIALOG_OK_BUTTON, timeout=5)
        if self.is_visible(self.CHECK_UPDATES_TITLE, timeout=5):
            self.tap(self.DIALOG_NO_BUTTON, timeout=5)

    def is_loaded(self) -> bool:
        self.dismiss_startup_dialogs()
        return self.is_visible(self.DRAWER_BUTTON, timeout=20)

    def open_drawer(self) -> None:
        self.dismiss_startup_dialogs()
        self.tap(self.DRAWER_BUTTON, timeout=20)

    def open_settings(self) -> SettingsPage:
        self.tap(self.SETTINGS_MENU_ITEM, timeout=20)
        return SettingsPage(self.driver)

    def open_about(self) -> AboutPage:
        self.tap(self.ABOUT_MENU_ITEM, timeout=20)
        return AboutPage(self.driver)
