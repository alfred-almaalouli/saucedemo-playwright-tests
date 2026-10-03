import re

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Covers the three checkout steps: information, overview and complete."""

    path = "/checkout-step-one.html"

    def __init__(self, page):
        super().__init__(page)
        # step one - customer information
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.error_message = page.locator("[data-test='error']")
        # step two - overview
        self.subtotal_label = page.locator("[data-test='subtotal-label']")
        self.tax_label = page.locator("[data-test='tax-label']")
        self.total_label = page.locator("[data-test='total-label']")
        self.finish_button = page.locator("[data-test='finish']")
        # complete
        self.complete_header = page.locator("[data-test='complete-header']")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    @staticmethod
    def _amount(text: str) -> float:
        return float(re.search(r"\$([\d.]+)", text).group(1))

    def subtotal(self) -> float:
        return self._amount(self.subtotal_label.inner_text())

    def tax(self) -> float:
        return self._amount(self.tax_label.inner_text())

    def total(self) -> float:
        return self._amount(self.total_label.inner_text())

    def finish(self):
        self.finish_button.click()
