import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_login_positive_valid_user(self, driver):
        login_page = LoginPage(driver)

        # 1. Arrange dan Act
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # 2. Assertions
        expected_inventory_url = "https://www.saucedemo.com/inventory.html"
        actual_url = login_page.get_current_url()

        # Assertion 1: Validasi perubahan URL
        assert actual_url == expected_inventory_url, (f"Kegagalan URL: Diharapkan '{expected_inventory_url}', tetapi berada di '{actual_url}'")

        # Assertation 2: Validasi keberadaan elemen penanda dashboard berhasil login
        assert login_page.is_dashboard_displayed() is True, (
            "Dashboard Swag Labs logo tidak tampil setelah submit login valid!"
        )

    def test_login_negative_locked_out_user(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        #Assertion: Validasi teks pesan kesalahan
        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message()

        assert expected_error in actual_error, ( f"Pesan error tidak sesuai. Diharapkan: '{expected_error}', Diterima:{actual_error}'")

    def test_login_negative_empty_password(self, driver):
        login_page = LoginPage(driver)

        login_page.open()
        login_page.login("standard_user", "")

        expected_error = "Epic sadface: Password is required"
        actual_error = login_page.get_error_message()

        assert expected_error in actual_error, (f"Validasi form kosong gagal. Diharapkan: '{expected_error}', Diterima:{actual_error}'")