import clipboard
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from core.locators.homepage_locators import HomepageLocators
from core.services.email_service import EmailService
from core.utility.utilities import UtilityMethods

locators = HomepageLocators()
url = "https://www.youtube.com/"


class Test_Share_Button:
    @pytest.mark.skip("")
    def test_open_youtube(self, browser) -> None:
        browser.get(url)
        title = browser.title
        assert "YouTube" in title

    def test_search_field(self, browser) -> None:
        browser.get(url)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.search_field))) \
            .send_keys("pytest")
        browser.find_element_by_css_selector(locators.search_button).click()
        elem = browser.find_elements_by_id(locators.video_title)[0]
        url_first_video_after_search = elem.get_attribute(locators.video_href)
        print("First video URL is: " + url_first_video_after_search)
        assert url_first_video_after_search is not None or ""
        browser.get(url_first_video_after_search)

    def test_share_button_url(self, browser) -> None:
        browser.get(url)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locators.search_field))) \
            .send_keys("pytest")
        browser.find_element_by_css_selector(locators.search_button).click()
        elem = browser.find_elements_by_id(locators.video_title)[0]
        url_first_video_after_search = elem.get_attribute(locators.video_href)
        print("URL of video after search: " + url_first_video_after_search)
        assert url_first_video_after_search is not None or ""
        browser.get(url_first_video_after_search)
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locators.share_button))).click()

        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, locators.copy_button_inside_container)))
        browser.find_element_by_css_selector(locators.copy_button_inside_container).click()

        shared_url = clipboard.paste()
        print("URL of video after share copy:" + shared_url)

        assert UtilityMethods.str_to_video_name(url_first_video_after_search) == \
               UtilityMethods.str_to_video_name(shared_url)
        EmailService.send_email(shared_url)
