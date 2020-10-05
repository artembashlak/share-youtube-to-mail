from abc import abstractmethod

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.get_base_url())

    def wait_and_find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    @abstractmethod
    def get_base_url(self):
        raise NotImplementedError('Abstract base class')
