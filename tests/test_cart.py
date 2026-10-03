import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage


@pytest.mark.smoke
def test_add_one_product_updates_badge(logged_in):
    logged_in.add_to_cart("Sauce Labs Backpack")

    expect(logged_in.cart_badge).to_have_text("1")


@pytest.mark.regression
def test_add_and_remove_products(logged_in):
    logged_in.add_to_cart("Sauce Labs Backpack")
    logged_in.add_to_cart("Sauce Labs Bike Light")
    expect(logged_in.cart_badge).to_have_text("2")

    logged_in.remove_from_cart("Sauce Labs Backpack")
    expect(logged_in.cart_badge).to_have_text("1")

    logged_in.remove_from_cart("Sauce Labs Bike Light")
    expect(logged_in.cart_badge).to_have_count(0)


@pytest.mark.regression
def test_cart_shows_selected_products(logged_in, page):
    selected = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for name in selected:
        logged_in.add_to_cart(name)
    logged_in.go_to_cart()

    cart = CartPage(page)
    expect(cart.items).to_have_count(len(selected))
    assert sorted(cart.names()) == sorted(selected)


@pytest.mark.regression
def test_cart_is_kept_after_reload(logged_in, page):
    logged_in.add_to_cart("Sauce Labs Fleece Jacket")
    page.reload()

    expect(logged_in.cart_badge).to_have_text("1")
