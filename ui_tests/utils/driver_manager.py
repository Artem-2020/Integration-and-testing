import os
from selenium import webdriver

def get_driver(browser="edge"):
    try:
        if browser == "chrome":
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)

        else:
            from selenium.webdriver.edge.service import Service
            from webdriver_manager.microsoft import EdgeChromiumDriverManager

            service = Service(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)

    except Exception:
        # fallback если нет интернета
        if browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()

    driver.maximize_window()
    return driver