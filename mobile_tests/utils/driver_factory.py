from __future__ import annotations

from appium import webdriver
from appium.options.android import UiAutomator2Options

from config import AppConfig


def build_android_options(config: AppConfig) -> UiAutomator2Options:
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = config.device_name
    options.app_package = config.app_package
    options.app_activity = config.main_activity
    options.app_wait_activity = config.app_wait_activity
    options.no_reset = config.no_reset
    options.auto_grant_permissions = config.auto_grant_permissions
    options.new_command_timeout = config.new_command_timeout
    options.language = config.language
    options.locale = config.locale
    if config.build_tools_version:
        options.set_capability("appium:buildToolsVersion", config.build_tools_version)

    if config.udid:
        options.udid = config.udid

    if config.apk_path.exists():
        options.app = str(config.apk_path)

    return options


def create_android_driver(config: AppConfig) -> webdriver.Remote:
    options = build_android_options(config)
    return webdriver.Remote(command_executor=config.appium_server_url, options=options)
