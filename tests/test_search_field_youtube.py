import clipboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from core.services.email_service import EmailService
from core.utility.utilities import UtilityMethods

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")


# @pytest.mark.skip(".")
def test_open_youtube():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://www.youtube.com/")
    title = driver.title
    assert "YouTube" in title
    driver.close()


# @pytest.mark.skip("..")
def test_search_field():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://www.youtube.com/")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys("pytest")
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    elem = driver.find_elements_by_id("video-title")[0]
    url_first_video_after_search = elem.get_attribute("href")
    print("First video URL is: " + url_first_video_after_search)
    assert url_first_video_after_search is not None or ""
    driver.get(url_first_video_after_search)
    driver.quit()


# @pytest.mark.skip("...")
def test_share_button_url():
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://www.youtube.com/")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys("pytest")
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    elem = driver.find_elements_by_id("video-title")[0]
    url_first_video_after_search = elem.get_attribute("href")
    print("URL of video after search: " + url_first_video_after_search)
    assert url_first_video_after_search is not None or ""
    driver.get(url_first_video_after_search)
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-container .size-default:nth-child(3)"))).click()
    copy_button = "#copy-button #text"

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, copy_button)))
    driver.find_element_by_css_selector(copy_button).click()

    shared_url = clipboard.paste()
    print("URL of video after share copy:" + shared_url)

    assert UtilityMethods.str_to_video_name(url_first_video_after_search) == \
           UtilityMethods.str_to_video_name(shared_url)
    EmailService.send_email(shared_url)

    driver.quit()
