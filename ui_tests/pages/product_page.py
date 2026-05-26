# pages/product_page.py

from pages.base_page import BasePage

class ProductPage(BasePage):

    def add_to_cart(self):
        self.wait.until(lambda d: d.execute_script("""
            const app = document.querySelector('shop-app');
            if (!app) return false;

            const shadow1 = app.shadowRoot;
            if (!shadow1) return false;

            const pages = shadow1.querySelector('iron-pages');
            if (!pages) return false;

            const detail = pages.querySelector('shop-detail');
            if (!detail) return false;

            const shadow2 = detail.shadowRoot;
            if (!shadow2) return false;

            const btn = shadow2.querySelector('button');
            if (!btn) return false;

            btn.click();
            return true;
        """))
    
    def wait_for_detail(self):
        self.wait.until(lambda d: d.execute_script("""
            const app = document.querySelector('shop-app');
            if (!app) return false;

            const pages = app.shadowRoot.querySelector('iron-pages');
            if (!pages) return false;

            return pages.querySelector('shop-detail') !== null;
        """))