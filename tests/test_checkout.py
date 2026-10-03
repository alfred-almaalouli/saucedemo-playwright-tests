import re

import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from tests.test_data import CUSTOMER, PRODUCTS, TAX_RATE


def _go_to_checkout(inventory, page, products):
    for name in products:
        inventory.add_to_cart(name)
    inventory.go_to_cart()
    CartPage(page).checkout()
    return CheckoutPage(page)


@pytest.mark.smoke
def test_complete_order_end_to_end(logged_in, page):
    checkout = _go_to_checkout(logged_in, page, ["Sauce Labs Backpack"])
    checkout.fill_information(**CUSTOMER)
    checkout.finish()

    expect(page).to_have_url(re.compile(r".*/checkout-complete\.html$"))
    expect(checkout.complete_header).to_have_text("Thank you for your order!")


@pytest.mark.regression
def test_order_totals_are_calculated_correctly(logged_in, page):
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Onesie"]
    checkout = _go_to_checkout(logged_in, page, products)
    checkout.fill_information(**CUSTOMER)

    expected_subtotal = round(sum(PRODUCTS[p] for p in products), 2)
    expected_tax = round(expected_subtotal * TAX_RATE, 2)

    assert checkout.subtotal() == expected_subtotal
    assert checkout.tax() == expected_tax
    assert checkout.total() == round(expected_subtotal + expected_tax, 2)


@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        ("", "Tester", "45143", "Error: First Name is required"),
        ("Alfred", "", "45143", "Error: Last Name is required"),
        ("Alfred", "Tester", "", "Error: Postal Code is required"),
    ],
    ids=["missing-first-name", "missing-last-name", "missing-postal-code"],
)
def test_checkout_form_validation(logged_in, page, first_name, last_name, postal_code,
                                  expected_error):
    checkout = _go_to_checkout(logged_in, page, ["Sauce Labs Backpack"])
    checkout.fill_information(first_name, last_name, postal_code)

    expect(checkout.error_message).to_have_text(expected_error)
