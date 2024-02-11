class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
        self.hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"

    # metoda zwraca liste wyszukanych hoteli
    def get_hotel_names(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        return [hotel.get_attribute("textContent") for hotel in hotels]

    # matoda zwraca liste cen hoteli
    def get_hotel_prices(self):
        prices = self.driver.find_elements("xpath", self.hotel_prices_xpath)
        return [price.get_attribute('textContent') for price in prices]
