from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


@dataclass(frozen=True)
class AppConfig:
    project_root: Path
    appium_server_url: str
    device_name: str
    udid: str | None
    app_package: str
    main_activity: str
    about_activity: str
    settings_activity: str
    app_wait_activity: str
    apk_path: Path
    language: str
    locale: str
    build_tools_version: str | None
    no_reset: bool
    auto_grant_permissions: bool
    new_command_timeout: int
    screenshots_dir: Path

    @classmethod
    def from_env(cls) -> "AppConfig":
        project_root = Path(__file__).resolve().parent
        apk_default = project_root / "artifacts" / "NewPipe_v0.28.7.apk"
        screenshots_dir = project_root / "artifacts" / "screenshots"
        return cls(
            project_root=project_root,
            appium_server_url=os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723"),
            device_name=os.getenv("DEVICE_NAME", "Android Emulator"),
            udid=os.getenv("UDID"),
            app_package=os.getenv("APP_PACKAGE", "org.schabi.newpipe"),
            main_activity=os.getenv("MAIN_ACTIVITY", "org.schabi.newpipe.MainActivity"),
            about_activity=os.getenv(
                "ABOUT_ACTIVITY", "org.schabi.newpipe.about.AboutActivity"
            ),
            settings_activity=os.getenv(
                "SETTINGS_ACTIVITY", "org.schabi.newpipe.settings.SettingsActivity"
            ),
            app_wait_activity=os.getenv("APP_WAIT_ACTIVITY", "org.schabi.newpipe.*"),
            apk_path=Path(os.getenv("APK_PATH", str(apk_default))).resolve(),
            language=os.getenv("APP_LANGUAGE", "en"),
            locale=os.getenv("APP_LOCALE", "US"),
            build_tools_version=os.getenv("BUILD_TOOLS_VERSION", "36.1.0"),
            no_reset=_as_bool(os.getenv("NO_RESET"), False),
            auto_grant_permissions=_as_bool(
                os.getenv("AUTO_GRANT_PERMISSIONS"), True
            ),
            new_command_timeout=int(os.getenv("NEW_COMMAND_TIMEOUT", "240")),
            screenshots_dir=screenshots_dir,
        )

    def ensure_directories(self) -> None:
        self.screenshots_dir.mkdir(parents=True, exist_ok=True)


CONFIG = AppConfig.from_env()
