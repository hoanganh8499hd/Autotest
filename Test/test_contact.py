import time
import unittest
import chromedriver_autoinstaller
from selenium import webdriver
from Pages.ContactUs import ContactUS

chromedriver_autoinstaller.install()


class ContactUs(unittest.TestCase):

    def setUp(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()

    def test_contact(self):
        email = 'admin@gmail.com'
        order = '26'
        message = 'Test Contact Pytest Python'
        ct = ContactUS(self.driver)
        ct.click_contact()
        time.sleep(3)
        ct.set_subject()
        ct.set_email(email)
        ct.set_order(order)
        ct.set_message(message)
        time.sleep(3)
        ct.click_sendms()
        time.sleep(4)

        if self.driver.find_element_by_xpath('//*[@id="center_column"]/p'):
            print('Successful')
        else:
            print('False')

    def tearDown(self):
        self.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()
