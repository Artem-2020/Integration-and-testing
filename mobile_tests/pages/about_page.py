from __future__ import annotations

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class AboutPage(BasePage):
    ABOUT_TITLE = BasePage.text_locator("About NewPipe")
    ABOUT_TAB = BasePage.text_locator("ABOUT & FAQ")
    LICENSES_TAB = BasePage.text_locator("LICENSES")
    VERSION_LABEL = (AppiumBy.ID, "org.schabi.newpipe:id/about_app_version")

    def is_loaded(self) -> bool:
        return self.is_visible(self.ABOUT_TITLE, timeout=20) and self.is_visible(
            self.VERSION_LABEL, timeout=5
        )

    def has_expected_content(self) -> bool:
        return (
            self.is_visible(self.ABOUT_TAB, timeout=5)
            and self.is_visible(self.LICENSES_TAB, timeout=5)
            and self.is_visible(self.VERSION_LABEL, timeout=5)
        )
