import re

import pytest
from playwright.sync_api import expect

from tests.test_data import LOCKED_OUT_USER, PASSWORD, STANDARD_USER


@pytest.mark.smoke
def test_valid_login_opens_products_page(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)

    expect(page).to_have_url(re.compile(r".*/inventory\.html$"))
    expect(page.locator("[data-test='title']")).to_have_text("Products")


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("", "", "Epic sadface: Username is required"),
        (STANDARD_USER, "", "Epic sadface: Password is required"),
        ("", PASSWORD, "Epic sadface: Username is required"),
        (STANDARD_USER, "wrong_password",
         "Epic sadface: Username and password do not match any user in this service"),
        ("unknown_user", PASSWORD,
         "Epic sadface: Username and password do not match any user in this service"),
    ],
    ids=["empty-fields", "empty-password", "empty-username", "wrong-password", "unknown-user"],
)
def test_invalid_login_shows_error(login_page, username, password, expected_error):
    login_page.login(username, password)

    expect(login_page.error_message).to_have_text(expected_error)


@pytest.mark.regression
def test_locked_out_user_cannot_login(login_page):
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    expect(login_page.error_message).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


@pytest.mark.regression
def test_logout_returns_to_login_page(logged_in, page):
    logged_in.logout()

    expect(page.locator("[data-test='login-button']")).to_be_visible()


@pytest.mark.regression
def test_products_page_is_protected_without_login(page):
    page.goto("/inventory.html")

    expect(page.locator("[data-test='error']")).to_contain_text(
        "You can only access '/inventory.html' when you are logged in"
    )
