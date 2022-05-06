import time
import json
import unittest
from Pages.OrderPage import OrderPage
import chromedriver_autoinstaller
from selenium import webdriver

chromedriver_autoinstaller.install()


class TestOrder(unittest.TestCase):

    def get_userlogin_data():
        with open('../Data/userlogin.json', 'r') as openfile:
            json_object = json.load(openfile)
        return json_object

    global json_object, email, pw
    json_object = get_userlogin_data()
    email = json_object['email']
    pw = json_object['psw']

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')

        print('Test start')
        print('-------------------------')

    def test_orderPro(self):
        check_order = OrderPage(self.driver)
        check_order.hover_product1()
        time.sleep(3)
        check_order.click_continue_shopping()
        time.sleep(3)
        check_order.hover_product2()
        time.sleep(3)
        check_order.click_continue_shopping()
        time.sleep(3)
        check_order.hover_product3()
        time.sleep(3)
        check_order.click_checkout()
        time.sleep(3)
        total_product = check_order.total_price()
        time.sleep(3)
        all_total_product = check_order.amount_total_product()
        if total_product == all_total_product:
            print('Amount total is True')
        else:
            print('Amount total is False')
        check_order.click_proceed_checkout()
        time.sleep(2)
        check_order.input_email(email)
        check_order.input_pass(pw)
        time.sleep(2)
        check_order.click_signIn()
        time.sleep(2)
        check_order.click_proceed_checkout2()
        time.sleep(2)
        check_order.click_checkterm()
        time.sleep(2)
        check_order.click_proceed_checkout3()
        time.sleep(2)
        check_order.chose_payment_method()
        time.sleep(2)
        check_order.click_confirm()
        time.sleep(2)
        title = check_order.check_notice_success()
        self.assertEqual('Your order on My Store is complete.',
                         title, 'This notice is matching')
        time.sleep(10)

    def test_changeOrderDetail(self):
        value = 3
        change_order = OrderPage(self.driver)
        change_order.hover_product1()
        time.sleep(2)
        change_order.click_continue_shopping()
        time.sleep(1)
        change_order.hover_product2()
        time.sleep(2)
        change_order.click_continue_shopping()
        time.sleep(1)
        change_order.hover_product3()
        time.sleep(2)
        change_order.click_continue_shopping()
        time.sleep(1)
        change_order.hover_product4()
        time.sleep(2)
        change_order.click_continue_shopping()
        time.sleep(1)
        change_order.hover_product5()
        time.sleep(2)
        change_order.click_checkout()
        time.sleep(3)
        list_deleted = []
        change_order.choice_random(list_deleted, value)
        time.sleep(2)
        change_order.delete_random(list_deleted)

        change_order.click_proceed_checkout()
        change_order.input_email(email)
        change_order.input_pass(pw)
        change_order.click_signIn()
        change_order.click_proceed_checkout2()
        change_order.click_proceed_checkout3()

        alert_term = change_order.check_alert_term()
        self.assertEqual('You must agree to the terms of service before continuing.', alert_term,
                         'This alert does not matching')

        self.driver.find_element_by_xpath(
            '//*[@id="order"]/div[2]/div/div/a').click()
        time.sleep(3)
        change_order.click_checkterm()
        time.sleep(2)
        change_order.click_proceed_checkout3()
        change_order.chose_payment_method()
        change_order.click_confirm()
        title = change_order.check_notice_success()
        self.assertEqual('Your order on My Store is complete.',
                         title, 'This notice is matching')
        time.sleep(10)

    # # Check sale order
    def test_sale_product(self):
        get_sale_product = OrderPage(self.driver)
        lst_product = get_sale_product.check_sale_product()
        sale_product = '-20%'
        for i in lst_product:
            if sale_product in i.text:
                i.click()
                time.sleep(4)
                get_sale_product.add_toCart()
                get_sale_product.checkout()
                get_sale_product.click_proceed_checkout()
                get_sale_product.input_email(email)
                get_sale_product.input_pass(pw)
                get_sale_product.click_signIn()
                get_sale_product.click_proceed_checkout2()
                get_sale_product.click_checkterm()
                time.sleep(2)
                get_sale_product.click_proceed_checkout3()
                get_sale_product.chose_payment_method()
                get_sale_product.click_confirm()
                title = get_sale_product.check_notice_success()
                self.assertEqual(
                    'Your order on My Store is complete.', title, 'This notice is matching')
                time.sleep(10)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        print('-------------------------')
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
