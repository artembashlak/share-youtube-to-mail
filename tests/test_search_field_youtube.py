import clipboard
import pytest

from core.pages.main_youtube_page import MainYoutubePage, SEARCH_FIELD, SEARCH_BUTTON
from core.pages.search_results_page import VIDEO_TITLE, SearchResultsPage
from core.pages.video_player_page import SHARE_BUTTON, COPY_BUTTON
from core.services.email_service import EmailService
from core.utility.utilities import str_to_video_name


class TestShareButton:
    @pytest.mark.skip("Skip long test")
    def test_youtube_title(self, browser) -> None:
        youtube_page = MainYoutubePage(browser)
        assert "YouTube" in youtube_page.get_page_title()

    def test_share_button_url(self, browser):
        youtube_page = MainYoutubePage(browser)
        youtube_page.send_text(SEARCH_FIELD, "pytest")
        youtube_page.click(SEARCH_BUTTON)
        url_first_video_after_search = youtube_page.get_link(VIDEO_TITLE, "href")
        print("URL of video after search: " + url_first_video_after_search)
        assert url_first_video_after_search is not None or ""

        SearchResultsPage(browser).click_first_video(url_first_video_after_search)
        youtube_page.click(SHARE_BUTTON)
        youtube_page.click(COPY_BUTTON)

        shared_url = clipboard.paste()
        print("URL of video after share copy:" + shared_url)

        assert str_to_video_name(url_first_video_after_search) == str_to_video_name(shared_url)
        EmailService.send_email(shared_url)
