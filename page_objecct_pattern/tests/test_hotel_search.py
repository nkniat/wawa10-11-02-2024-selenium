import pytest
from selenium import webdriver
from page_objecct_pattern.pages.search_hotel import SearchHotelPage
from page_objecct_pattern.pages.search_results import SearchResultsPage
class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/")
        search_hotel_page = SearchHotelPage(self.driver)
        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("14/02/2024", "17/02/2024")
        search_hotel_page.set_travellers("2","0")
        search_hotel_page.perform_search()

        results_page = SearchResultsPage(self.driver)
        hotel_names = results_page.get_hotel_names()
        hotel_prices = results_page.get_hotel_prices()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        assert hotel_prices[0] == "£14.30"
        assert hotel_prices[1] == "£32.50"
        assert hotel_prices[2] == "£52"
        assert hotel_prices[3] == "£97.50"
