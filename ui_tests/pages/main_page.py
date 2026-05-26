from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def open(self, url="https://shop.polymer-project.org/"):
        self.driver.get(url)

    def go_to_men(self):
        self.driver.execute_script("""
            const app = document.querySelector('shop-app');
            if (!app) return;

            const pages = app.shadowRoot.querySelector('iron-pages');
            if (!pages) return;

            const home = pages.querySelector('shop-home');
            if (!home) return;

            const link = home.shadowRoot.querySelector('a[href="/list/mens_outerwear"]');
            if (link) link.click();
        """)

        self.wait.until(lambda d: d.execute_script("""
            const app = document.querySelector('shop-app');
            if (!app) return false;

            const pages = app.shadowRoot.querySelector('iron-pages');
            if (!pages) return false;

            return pages.querySelector('shop-list') !== null;
        """))

    def open_first_item(self):
        self.wait.until(lambda d: d.execute_script("""
            const app = document.querySelector('shop-app');
            if (!app) return false;

            const shadow1 = app.shadowRoot;
            if (!shadow1) return false;

            const pages = shadow1.querySelector('iron-pages');
            if (!pages) return false;

            const list = pages.querySelector('shop-list');
            if (!list) return false;

            const shadow2 = list.shadowRoot;
            if (!shadow2) return false;

            const item = shadow2.querySelector('a[href*="detail"]');
            if (!item) return false;

            item.click();
            return true;
        """))