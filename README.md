# Sauce Demo – UI Test Automation

![UI Tests](https://github.com/alfred-almaalouli/saucedemo-playwright-tests/actions/workflows/tests.yml/badge.svg)

Automated end-to-end UI tests for the [Sauce Demo](https://www.saucedemo.com) web shop, written in **Python** with **Playwright** and **pytest**.

The project shows how I approach test automation: clear test cases first, a maintainable **Page Object Model**, data-driven tests, readable HTML reports and tests that run automatically in **GitHub Actions** on every push.

## What is tested

24 automated tests covering the main user flows:

| Area | What is checked |
|------|-----------------|
| Login | Valid login, empty fields, wrong password, unknown user, locked-out user, logout, protected pages |
| Products | All products listed, prices, sorting by name and price (4 options) |
| Cart | Add / remove products, cart badge, cart content, cart kept after reload |
| Checkout | Full order end to end, subtotal + 8 % tax + total, form validation |

All test cases with IDs, priority and test design technique (equivalence partitioning, boundary values, decision table) are listed in [docs/test-cases.md](docs/test-cases.md).

## Tech stack

- Python 3.12
- Playwright (Chromium)
- pytest + pytest-playwright
- pytest-html (HTML report)
- GitHub Actions (CI)

## Project structure

```
pages/                  Page Object Model – one class per page
  base_page.py
  login_page.py
  inventory_page.py
  cart_page.py
  checkout_page.py
tests/
  conftest.py           shared fixtures (e.g. logged-in user)
  test_data.py          users, products, prices, customer data
  test_login.py
  test_inventory.py
  test_cart.py
  test_checkout.py
docs/test-cases.md      test case overview
.github/workflows/      CI pipeline
```

## Run the tests

```bash
pip install -r requirements.txt
python -m playwright install chromium

pytest                       # all tests (headless)
pytest -m smoke              # only the smoke tests
pytest --headed --slowmo 300 # watch the browser while the tests run
```

After a run, the HTML report is in `reports/report.html`.
In GitHub Actions the report is uploaded as an artifact (`test-report`) for every run.

## Design decisions

- **Page Object Model** – locators and page actions live in `pages/`, so a change in the UI only needs to be fixed in one place.
- **Stable locators** – tests use the `data-test` attributes of the site instead of CSS classes or text.
- **Data-driven tests** – `pytest.mark.parametrize` runs one test with many input combinations (login errors, sorting options, checkout form).
- **Web-first assertions** – Playwright's `expect()` waits automatically, so there are no fixed `sleep()` calls.
- **Smoke vs. regression** – markers allow a quick smoke run or the full regression suite.

## Author

Alfred Al Maalouli – [GitHub](https://github.com/alfred-almaalouli)
