import unittest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.delivery_date_page import DeliveryDatePage


class CarrefourPurchase(unittest.TestCase):

    CARREFOUR_URL = "https://www.carrefour.pl/"

    def setUp(self):
        self.main_page = MainPage()
        self.login_page = LoginPage()
        self.delivery_date_page = DeliveryDatePage()
        self.main_page.go_to_url(self.CARREFOUR_URL)

    def test_purchase(self):
        self.main_page.agreement_confirmation()
        self.main_page.navigate_to_login_page()
        self.login_page.login()
        self.delivery_date_page.delivery_type_picker()
        self.delivery_date_page.booking_the_delivery_date()
        self.main_page.add_products_to_basket()

    def tearDown(self):
        self.main_page.quit_driver()


if __name__ == '__main__':
    unittest.main()
