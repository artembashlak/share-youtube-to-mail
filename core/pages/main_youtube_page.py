from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage

SEARCH_FIELD = (By.CSS_SELECTOR, "input#search")
SEARCH_BUTTON = (By.CSS_SELECTOR, "button.style-scope.ytd-searchbox#search-icon-legacy")


class MainYoutubePage(BasePage):

    def get_page_title(self):
        title = self.driver.title
        return title

    def send_text(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    def click(self, locator):
        self.wait_and_find_element(locator).click()

    def get_link(self, locator, attr):
        return self.driver.find_elements_by_css_selector(locator)[0].get_attribute(attr)

    def get_base_url(self):
        return "https://www.youtube.com/"
