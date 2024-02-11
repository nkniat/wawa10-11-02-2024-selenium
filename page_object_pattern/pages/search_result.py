import logging
from page_object_pattern.locators.locators import SearchResultLocators


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
        self.hotel_prices_xpath = SearchResultLocators.hotel_prices_xpath

        # self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        # self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"

    # metoda zwraca liste wyszukanych hoteli
    def get_hotel_names(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]

        self.logger.info("Names of hotels are: ")
        for name in names:
            self.logger.info(name)

        return names

    # matoda zwraca liste cen hoteli
    def get_hotel_prices(self):
        prices = self.driver.find_elements("xpath", self.hotel_prices_xpath)
        prices = [price.get_attribute('textContent') for price in prices]

        self.logger.info("Prices of hotels are: ")
        for price in prices:
            self.logger.info(price)

        return prices
