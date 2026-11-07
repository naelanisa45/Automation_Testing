
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestInventory:

    def test_add_backpack_to_cart(self, driver):
        # Login
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Tambahkan backpack ke keranjang
        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

        # Validasi jumlah barang
        actual_count = inventory_page.get_cart_badge_count()

        assert actual_count == "1", (
            f"Jumlah barang tidak sesuai. "
            f"Diharapkan: '1', Diterima: '{actual_count}'"
        )

    def test_back_to_login_page(self, driver):
        # Login terlebih dahulu
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Kembali ke halaman login
        driver.get("https://www.saucedemo.com/")

        expected_url = "https://www.saucedemo.com/"
        actual_url = driver.current_url

        # Validasi URL
        assert actual_url == expected_url, (
            f"URL tidak sesuai. Diharapkan: '{expected_url}', "
            f"Diterima: '{actual_url}'"
        )

        # Validasi tombol Login tampil
        assert login_page.is_login_button_displayed() is True
