from settings import USER_LOGIN, USER_PASSWORD
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    __USERNAME_FIELD = (By.XPATH, "//input[@id='username']")
    __PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    __SUBMIT_BUTTON = (By.XPATH, "//input[@name='submit']")

    def login(self):
        self.fill(self.__USERNAME_FIELD, USER_LOGIN)
        self.fill(self.__PASSWORD_FIELD, USER_PASSWORD)
        self.click(self.__SUBMIT_BUTTON)
