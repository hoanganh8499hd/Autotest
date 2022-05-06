from selenium.webdriver.support.select import Select


class ContactUS:
    click_contact_xpath = '//*[@id="contact-link"]'
    input_subject_id = 'id_contact'
    input_email_id = 'email'
    input_order_id = 'id_order'
    input_fileup_id = 'fileUpload'
    input_message_id = 'message'
    click_send_id = 'submitMessage'

    def __init__(self, driver):
        self.driver = driver

    def click_contact(self):
        self.driver.find_element_by_xpath(self.click_contact_xpath).click()

    def set_subject(self):
        elt = self.driver.find_element_by_id(self.input_subject_id)
        drp = Select(elt)
        drp.select_by_value('1')

    def set_email(self, email):
        self.driver.find_element_by_id(self.input_email_id).send_keys(email)

    def set_order(self, order):
        self.driver.find_element_by_id(self.input_order_id).send_keys(order)

    def set_upload(self):
        self.driver.find_element_by_id(
            self.input_fileup_id).send_keys('img url in computer')

    def set_message(self, message):
        self.driver.find_element_by_id(
            self.input_message_id).send_keys(message)

    def click_sendms(self):
        self.driver.find_element_by_id(self.click_send_id).click()
