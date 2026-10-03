from pages.base_page import BasePage


class InventoryPage(BasePage):
    path = "/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator("[data-test='title']")
        self.items = page.locator("[data-test='inventory-item']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.item_prices = page.locator("[data-test='inventory-item-price']")
        self.sort_select = page.locator("[data-test='product-sort-container']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.menu_button = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("[data-test='logout-sidebar-link']")

    @staticmethod
    def _slug(product_name: str) -> str:
        # "Sauce Labs Backpack" -> "sauce-labs-backpack"
        return product_name.lower().replace(" ", "-")

    def add_to_cart(self, product_name: str):
        self.page.locator(f"[data-test='add-to-cart-{self._slug(product_name)}']").click()

    def remove_from_cart(self, product_name: str):
        self.page.locator(f"[data-test='remove-{self._slug(product_name)}']").click()

    def sort_by(self, option: str):
        # option values used by the site: az, za, lohi, hilo
        self.sort_select.select_option(option)

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.item_prices.all_inner_texts()]

    def go_to_cart(self):
        self.cart_link.click()

    def logout(self):
        self.menu_button.click()
        self.logout_link.click()
