import pytest
from playwright.sync_api import sync_playwright


def check_footer(page):

    footer = page.query_selector('footer')

    assert footer is not None, "Футер не найден на странице"
    assert page.query_selector(
        "footer a[href='https://www.awwwards.com/Ilyaredko/']") is not None, "Ссылка на Awwwards отсутствует"
    assert page.query_selector(
        "footer a[href='https://vk.com/onlydigitalagency']") is not None, "Ссылка на ВКонтакте отсутствует"
    assert page.query_selector(
        "footer a[href='https://t.me/onlycreativedigitalagency']") is not None, "Ссылка на Telegram отсутствует"
    assert page.query_selector(
        "footer a[href='https://vimeo.com/onlydigital']") is not None, "Ссылка на Vimeo отсутствует"
    assert page.query_selector(
        "footer a[href='https://www.behance.net/onlydigitalagency']") is not None, "Ссылка на Behance отсутствует"


PAGES_TO_TEST = [
    "https://only.digital/",
    "https://only.digital/projects/",
    "https://only.digital/company/"
]


@pytest.mark.parametrize("page_url", PAGES_TO_TEST)
def test_footer_on_page(page_url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(page_url)
        check_footer(page)
        browser.close()
