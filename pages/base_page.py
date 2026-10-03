from playwright.sync_api import Page


class BasePage:
    """Common helpers shared by all page objects."""

    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.path)
        return self
