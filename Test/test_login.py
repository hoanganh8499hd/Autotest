from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
import time
import unittest
# from parameterized import parameterized
from selenium import webdriver
import json
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()


class TestLogin(unittest.TestCase):

    def get_userlogin_data():
        with open('../Data/userlogin.json', 'r') as openfile:
            json_object = json.load(openfile)
        return json_object

    global json_object
    json_object = get_userlogin_data()

    def setUp(self):
        print("Test is started")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        time.sleep(3)
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_success(self):

        login = LoginPage(self.driver)
        login.clickSignIn()
        login.set_email(json_object['email'])
        login.set_psw(json_object['psw'])
        login.click_login()
        time.sleep(3)

    def test_login_unsuccessfully(self):

        login = LoginPage(self.driver)
        login.clickSignIn()
        login.set_email(json_object['email'])
        login.set_psw(json_object['psw'])
        login.click_login()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()
