class SearchHotelLocators:

    # wprowadzenie miasta
    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
    location_match_xpath = "//*[@id='select2-drop']/ul/li/ul/li/div/span"

    # daty przyjazdu i wyjazdu
    check_in_input_name = "checkin"
    check_out_input_name = "checkout"

    # kto jedzie?
    travellers_input_id = "travellersInput"
    adult_input_id = "adultInput"
    child_input_id = "childInput"

    # wyszukiwanie
    search_button_xpath = "//*[@id='hotels']/form/div[5]/button"


class SearchResultLocators:

    hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
    hotel_prices_xpath = "//div[contains(@class, 'price_tab')]//b"

