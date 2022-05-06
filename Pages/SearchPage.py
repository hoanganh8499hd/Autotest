class SearchPage:
    # Locator element
    input_search_id = 'search_query_top'

    def __init__(self, driver):
        self.driver = driver

    def click_search(self):
        self.driver.find_element_by_id(self.input_search_id).click()

    def input_something(self, something):
        self.driver.find_element_by_id(
            self.input_search_id).send_keys(something)

    def clear_search(self):
        self.driver.find_element_by_id(self.input_search_id).clear()

    def check_search(self):
        return self.driver.find_element_by_id(self.input_search_id).get_attribute('placeholder')
