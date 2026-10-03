# Test Cases – Sauce Demo

Test design techniques: **equivalence partitioning** (valid / invalid login data), **boundary values** (empty cart → 1 item → 0 items), **decision table** (required fields in the checkout form) and **end-to-end scenario** testing.

| ID | Area | Test case | Technique | Priority | Automated in |
|----|------|-----------|-----------|----------|--------------|
| TC-01 | Login | Valid user logs in and sees the "Products" page | Equivalence partitioning (valid class) | High | `test_login.py::test_valid_login_opens_products_page` |
| TC-02 | Login | Empty username and password show an error | Equivalence partitioning (invalid class) | High | `test_login.py::test_invalid_login_shows_error[empty-fields]` |
| TC-03 | Login | Empty password shows "Password is required" | Equivalence partitioning | Medium | `test_login.py::test_invalid_login_shows_error[empty-password]` |
| TC-04 | Login | Empty username shows "Username is required" | Equivalence partitioning | Medium | `test_login.py::test_invalid_login_shows_error[empty-username]` |
| TC-05 | Login | Wrong password is rejected | Equivalence partitioning | High | `test_login.py::test_invalid_login_shows_error[wrong-password]` |
| TC-06 | Login | Unknown user is rejected | Equivalence partitioning | Medium | `test_login.py::test_invalid_login_shows_error[unknown-user]` |
| TC-07 | Login | Locked-out user cannot log in | State-based | High | `test_login.py::test_locked_out_user_cannot_login` |
| TC-08 | Login | Logout returns to the login page | Scenario | Medium | `test_login.py::test_logout_returns_to_login_page` |
| TC-09 | Security | Products page cannot be opened without login | Negative test | High | `test_login.py::test_products_page_is_protected_without_login` |
| TC-10 | Products | All 6 products are listed | Requirement-based | High | `test_inventory.py::test_all_products_are_listed` |
| TC-11 | Products | Prices match the catalogue | Requirement-based | Medium | `test_inventory.py::test_product_prices_match_catalogue` |
| TC-12–15 | Products | Sorting A–Z, Z–A, price low–high, high–low | Equivalence partitioning (one test per option) | Medium | `test_inventory.py::test_sorting` |
| TC-16 | Cart | Adding a product updates the cart badge | Boundary value (0 → 1) | High | `test_cart.py::test_add_one_product_updates_badge` |
| TC-17 | Cart | Add and remove products, badge disappears at 0 | Boundary value (2 → 1 → 0) | Medium | `test_cart.py::test_add_and_remove_products` |
| TC-18 | Cart | Cart shows exactly the selected products | Requirement-based | High | `test_cart.py::test_cart_shows_selected_products` |
| TC-19 | Cart | Cart content is kept after page reload | State-based | Low | `test_cart.py::test_cart_is_kept_after_reload` |
| TC-20 | Checkout | Complete order end to end | End-to-end scenario | High | `test_checkout.py::test_complete_order_end_to_end` |
| TC-21 | Checkout | Subtotal, 8 % tax and total are correct | Requirement-based | High | `test_checkout.py::test_order_totals_are_calculated_correctly` |
| TC-22–24 | Checkout | Missing first name / last name / postal code shows an error | Decision table | Medium | `test_checkout.py::test_checkout_form_validation` |
