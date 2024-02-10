from page_objecct_pattern.locators.locators import SearchResultLocators
import logging

class SearchResultsPage:
    """
    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"
    """
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_names_xpath = SearchResultLocators.hotel_names_xpath
        self.hotel_prices_xpath = SearchResultLocators.hotel_prices_xpath

    def get_hotel_names(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        names = [hotel.get_attribute("textContent") for hotel in hotels]
        self.logger.info("Avialable hotels are:")
        for name in names:
            self.logger.info(name)
        return names
        #return [hotel.get_attribute("textContent") for hotel in hotels]

    def get_hotel_prices(self):
        prices = self.driver.find_elements("xpath", self.hotel_prices_xpath)
        prices = [price.get_attribute('textContent') for price in prices]
        self.logger.info("Avialable prices are:")
        for price in prices:
            self.logger.info(price)
        return prices
        #return [price.get_attribute('textContent') for price in prices]

