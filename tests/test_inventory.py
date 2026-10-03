import pytest
from playwright.sync_api import expect

from tests.test_data import PRODUCTS


@pytest.mark.smoke
def test_all_products_are_listed(logged_in):
    expect(logged_in.items).to_have_count(len(PRODUCTS))
    assert sorted(logged_in.names()) == sorted(PRODUCTS)


@pytest.mark.regression
def test_product_prices_match_catalogue(logged_in):
    shown = dict(zip(logged_in.names(), logged_in.prices()))
    assert shown == PRODUCTS


@pytest.mark.regression
@pytest.mark.parametrize(
    "option, key, reverse",
    [
        ("az", "name", False),
        ("za", "name", True),
        ("lohi", "price", False),
        ("hilo", "price", True),
    ],
    ids=["name-a-z", "name-z-a", "price-low-high", "price-high-low"],
)
def test_sorting(logged_in, option, key, reverse):
    logged_in.sort_by(option)

    values = logged_in.names() if key == "name" else logged_in.prices()
    assert values == sorted(values, reverse=reverse)
