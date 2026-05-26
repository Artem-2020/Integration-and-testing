from __future__ import annotations

from pages.base_page import BasePage


class SettingsPage(BasePage):
    SCREEN_TITLE = BasePage.text_locator("Settings")
    VIDEO_AUDIO_CATEGORY = BasePage.text_locator("Video and audio")
    APPEARANCE_CATEGORY = BasePage.text_locator("Appearance")
    DOWNLOAD_CATEGORY = BasePage.text_locator("Download")

    def is_loaded(self) -> bool:
        return self.is_visible(self.VIDEO_AUDIO_CATEGORY, timeout=20)

    def has_core_categories(self) -> bool:
        return (
            self.is_visible(self.VIDEO_AUDIO_CATEGORY, timeout=5)
            and self.is_visible(self.APPEARANCE_CATEGORY, timeout=5)
            and self.is_visible(self.DOWNLOAD_CATEGORY, timeout=5)
        )
