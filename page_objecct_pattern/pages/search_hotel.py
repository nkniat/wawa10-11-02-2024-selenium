import logging
from page_objecct_pattern.locators.locators import SearchHotelLocators

class SearchHotelPage:
    """
    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
        self.location_match_xpath = "//*[@id='select2-drop']/ul/li/ul/li/div/span"
        #self.location_match_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath =  "//*[@id='hotels']/form/div[5]/button"
        #self.search_button_xpath = "//button[text()=' Search']"
    """

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.location_match_xpath = SearchHotelLocators.location_match_xpath
        #self.location_match_xpath = SearchHotelLocators.location_match_xpath
        self.check_in_input_name = SearchHotelLocators.check_in_input_name
        self.check_out_input_name = SearchHotelLocators.check_out_input_name
        self.travellers_input_id = SearchHotelLocators.travellers_input_id
        self.adult_input_id = SearchHotelLocators.adult_input_id
        self.child_input_id = SearchHotelLocators.child_input_id
        self.search_button_xpath = SearchHotelLocators.search_button_xpath
        #self.search_button_xpath = SearchHotelLocators.search_button_xpath

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element("xpath", self.search_hotel_span_xpath).click()
        self.driver.find_element("xpath", self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element("xpath", self.location_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting check in {checkin} an {chckeout} dates".format(checkin=check_in, chckeout=check_out))
        self.driver.find_element("name", self.check_in_input_name).send_keys(check_in)
        self.driver.find_element("name", self.check_out_input_name).send_keys(check_out)

    def set_travellers(self, adults, child):
        self.logger.info("Setting travellers {adults} and {children}".format(adults=adults, children=child))
        self.driver.find_element("id", self.travellers_input_id).click()
        self.driver.find_element("id", self.adult_input_id).clear()
        self.driver.find_element("id", self.adult_input_id).send_keys(adults)
        self.driver.find_element("id", self.child_input_id).clear()
        self.driver.find_element("id", self.child_input_id).send_keys(child)

    def perform_search(self):
        self.logger.info("Performing search")
        self.driver.find_element("xpath", self.search_button_xpath).click()