from core.pages.base_page import BasePage

VIDEO_TITLE = "a#video-title"


class SearchResultsPage(BasePage):
    def get_base_url(self):
        pass

    def click_first_video(self, url):
        self.driver.get(url)
