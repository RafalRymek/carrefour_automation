from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class DeliveryDatePage(BasePage):

    __PICK_UP_FROM_SHOP_BUTTON = (By.XPATH, "//div[contains(text(),'Odbiór w punkcie')]")
    __PICK_DELIVERY = (By.XPATH, "//span[contains(text(),'Odbiór w punkcie') or contains(text(),'rozpocznij zakupy')]")
    __INPUT_SHOP_ADDRESS = (By.XPATH, "//input[contains(@placeholder,'wpisz lub wybierz z listy')]")
    __ZIP_CODE = (By.XPATH, "//input[@name='zipCode']")
    __DELIVERY_DATE = (By.XPATH, "//span[contains(.,'dostępny')]/parent::div")
    __FIRST_AVAILABLE_HOUR = (By.XPATH, "//div[contains(.,'0,00 zł')]/parent::label")
    __PURCHASE_START_BUTTON = (By.XPATH, "//span[contains(text(),'rozpocznij zakupy') or contains(text(),'kontynuuj')]")

    def delivery_type_picker(self):
        self.click(self.__PICK_DELIVERY)

    def booking_the_delivery_date(self):
        self.click(self.__PICK_UP_FROM_SHOP_BUTTON)
        self.fill(self.__INPUT_SHOP_ADDRESS, "Kraków, Pokoju 44 - Carrefour Kraków Plaza")
        self.click_keyboard_key(self.__INPUT_SHOP_ADDRESS, Keys.ARROW_UP)
        self.click_keyboard_key(self.__INPUT_SHOP_ADDRESS, Keys.ENTER)
        self.hover_over_on_element(self.__DELIVERY_DATE)
        self.click(self.__DELIVERY_DATE)
        self.hover_over_on_element(self.__FIRST_AVAILABLE_HOUR)
        self.click(self.__FIRST_AVAILABLE_HOUR)
        self.click(self.__PURCHASE_START_BUTTON)
