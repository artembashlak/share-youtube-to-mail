from selenium.webdriver.common.by import By

from core.pages.base_page import BasePage

SHARE_BUTTON = (By.CSS_SELECTOR, "#menu-container .size-default:nth-child(3)")
COPY_BUTTON = (By.CSS_SELECTOR, "#copy-button #text")


class VideoPlayerPage(BasePage):
    def click_button(self):
        pass

    def copy_to_clipboard(self):
        pass
