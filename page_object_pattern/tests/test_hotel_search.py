import pytest
from selenium import webdriver
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_result import SearchResultsPage

class TestHotelSearch:

    # dokorator testu; definicja ustawien, czyszczenie
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

        # wprowadzenie miasta
        search_hotel_page.set_city("Dubai")

        # wprowadzenie daty zameldowania i wymeldowania
        search_hotel_page.set_date_range("14/02/2024", "15/02/2024")

        # wprowadzenie liczby gości
        search_hotel_page.set_travellers("3", "1")

        # wyszukaj
        search_hotel_page.perform_search()

        # Czesc druga - wyswietlenie wyników
        search_result_page = SearchResultsPage(self.driver)
        hotels_name = search_result_page.get_hotel_names()
        prices_list = search_result_page.get_hotel_prices()

        # assercja - wykonanie testu
        # sprawdzenie nazw hotelu
        assert hotels_name[0] == "Jumeirah Beach Hotel"
        assert hotels_name[1] == "Oasis Beach Tower"
        assert hotels_name[2] == "Rose Rayhaan Rotana"
        assert hotels_name[3] == "Hyatt Regency Perth"

        # sprawdzenie cen za hotel
        assert prices_list[0] == "£14.30"
        assert prices_list[1] == "£32.50"
        assert prices_list[2] == "£52"
        assert prices_list[3] == "£97.50"
