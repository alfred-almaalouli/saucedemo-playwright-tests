import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from tests.test_data import PASSWORD, STANDARD_USER


@pytest.fixture
def login_page(page):
    return LoginPage(page).open()


@pytest.fixture
def logged_in(page):
    """Starts each test on the products page as the standard user."""
    LoginPage(page).open().login(STANDARD_USER, PASSWORD)
    inventory = InventoryPage(page)
    expect(inventory.title).to_have_text("Products")
    return inventory
