from __future__ import annotations

from datetime import datetime

import pytest

from config import CONFIG
from utils.driver_factory import create_android_driver

try:
    import allure
except ImportError:  # pragma: no cover
    allure = None


@pytest.fixture(scope="session")
def app_config():
    CONFIG.ensure_directories()
    return CONFIG


@pytest.fixture
def driver(app_config, request):
    driver_instance = create_android_driver(app_config)
    yield driver_instance

    rep_call = getattr(request.node, "rep_call", None)
    if rep_call and rep_call.failed:
        file_name = (
            f"{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        screenshot_path = app_config.screenshots_dir / file_name
        driver_instance.save_screenshot(str(screenshot_path))
        if allure is not None:
            allure.attach.file(
                str(screenshot_path),
                name=request.node.name,
                attachment_type=allure.attachment_type.PNG,
            )

    driver_instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
