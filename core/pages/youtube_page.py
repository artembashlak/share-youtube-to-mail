from core.pages.base_page import BasePage


class YoutubePage(BasePage):
    def get_page_title(self):
        title = self.driver.title
        return title

    def enter_word(self, word, locator):
        elem = self.find_element(locator)
        elem.click()
        elem.send_keys(word)
        return elem

    def click_element(self, locator):
        elem = self.find_element(locator)
        return elem.click()

    def get_first_element(self, locator):
        return self.find_element(locator)[0]
