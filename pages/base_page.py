from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class BasePage:
    class __WebDriver:
        def __init__(self):
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            # chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                           chrome_options=chrome_options)
            self.driver.implicitly_wait(3)
            self.driver.set_window_size(1440, 900)

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.__WebDriver().driver
        self.explicity_wait = WebDriverWait(
            driver=self.driver,
            timeout=5
        )

    def go_to_url(self, url):
        self.driver.get(url)

    def get_element(self, by_locator):
        self.explicity_wait.until(EC.presence_of_element_located(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator)

    def click(self, by_locator):
        self.explicity_wait.until(EC.element_to_be_clickable(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator).click()

    def fill(self, by_locator, value):
        self.explicity_wait.until(EC.presence_of_element_located(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        return self.driver.find_element(*by_locator).send_keys(value)

    def hover_over_on_element(self, by_locator):
        self.explicity_wait.until(EC.presence_of_element_located(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        element = self.driver.find_element(*by_locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def click_keyboard_key(self, by_locator, key_value):
        self.explicity_wait.until(EC.element_to_be_clickable(by_locator),
                                  message=f"{by_locator} element doesn't appear on the page")
        element = self.driver.find_element(*by_locator)
        element.send_keys(key_value)

    def quit_driver(self):
        self.driver.quit()
