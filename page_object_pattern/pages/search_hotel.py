from page_object_pattern.locators.locators import SearchHotelLocators


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver

        #wprowadzenie miasta
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.location_match_xpath = SearchHotelLocators.location_match_xpath

        # daty przyjazdu i wyjazdu
        self.check_in_input_name = SearchHotelLocators.check_in_input_name
        self.check_out_input_name = SearchHotelLocators.check_out_input_name

        # kto jedzie?
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        self.adult_input_id = SearchHotelLocators.adult_input_id
        self.child_input_id = SearchHotelLocators.child_input_id

        # wyszukiwanie
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

        """
        # wprowadzenie miasta
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
        self.location_match_xpath = "//*[@id='select2-drop']/ul/li/ul/li/div/span"
        # daty przyjazdu i wyjazdu
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        # kto jedzie?
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        # wyszukiwanie
        self.search_button_xpath = "//*[@id='hotels']/form/div[5]/button"
        """

    # metoda wprowadzająca dane miasto
    def set_city(self, city):
        self.driver.find_element("xpath", self.search_hotel_span_xpath).click()
        self.driver.find_element("xpath", self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element("xpath", self.location_match_xpath).click()

    # metoda ustawiajac czas przyjazdu i wyjazdu
    def set_date_range(self, check_in, check_out):
        self.driver.find_element("name", self.check_in_input_name).send_keys(check_in)
        self.driver.find_element("name", self.check_out_input_name).send_keys(check_out)

    # metoda ustawiajaca liczbe dorosłych i dzieci
    def set_travellers(self, adults, child):
        self.driver.find_element("id", self.travellers_input_id).click()
        # dorośli
        self.driver.find_element("id", self.adult_input_id).clear()
        self.driver.find_element("id", self.adult_input_id).send_keys(adults)
        # dzieci
        self.driver.find_element("id", self.child_input_id).clear()
        self.driver.find_element("id", self.child_input_id).send_keys(child)

    # metoda uruchamiajaca wyszukiwanie
    def perform_search(self):
        self.driver.find_element("xpath", self.search_button_xpath).click()
