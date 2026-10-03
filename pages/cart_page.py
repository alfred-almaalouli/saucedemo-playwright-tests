from pages.base_page import BasePage


class CartPage(BasePage):
    path = "/cart.html"

    def __init__(self, page):
        super().__init__(page)
        self.items = page.locator("[data-test='inventory-item']")
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping_button = page.locator("[data-test='continue-shopping']")

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def checkout(self):
        self.checkout_button.click()
