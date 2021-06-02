from selenium.webdriver.common.by import By
from settings import shopping_list
from pages.base_page import BasePage
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    __AGREEMENT_BUTTON = (By.XPATH, ".//span[contains(text(),'Wyrażam')]")
    __LOGIN_BUTTON = (By.XPATH, "//b[contains(text(),'Zaloguj')]")
    __SEARCH_FIELD_SELECTOR = (By.XPATH, "//input[@id='search-input']")
    __MAGNIFIER_ICON = (By.XPATH, "//*[@class='MuiButton-label']/*[@class='MuiSvgIcon-root']/.")
    __ADD_TO_BASKET = (By.XPATH, " //span[contains(text(),'Do koszyka') or normalize-space()='+']")

    def agreement_confirmation(self):
        self.click(self.__AGREEMENT_BUTTON)

    def navigate_to_login_page(self):
        self.click(self.__LOGIN_BUTTON)

    def search_for_product(self, product):
        self.fill(self.__SEARCH_FIELD_SELECTOR, product)
        self.click(self.__MAGNIFIER_ICON)

    def add_product_to_basket(self):
        try:
            self.click(self.__ADD_TO_BASKET)
        except StaleElementReferenceException:
            print("One product was missing from the shopping list")

    # clear method for windows
    # def clear_input_search_for_win(self):
    #     self.driver.find_element(*self.__SEARCH_FIELD_SELECTOR).send_keys(Keys.CONTROL, "a" + Keys.BACKSPACE)

    def clear_input_search_for_mac(self):
        element = self.driver.find_element(*self.__SEARCH_FIELD_SELECTOR)
        search_length = len(element.get_attribute('value'))
        element.send_keys(search_length * Keys.BACKSPACE)

    def add_products_to_basket(self):
        for product in shopping_list:
            self.search_for_product(product)
            self.add_product_to_basket()
            self.clear_input_search_for_mac()
