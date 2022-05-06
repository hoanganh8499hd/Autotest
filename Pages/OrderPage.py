import random

from selenium.webdriver import ActionChains


class OrderPage:
    # Locator
    # Test order Sucess
    product1_hover_xpath = '//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[1]/img'
    product2_hover_xpath = '//*[@id="homefeatured"]/li[1]/div/div[1]/div/a[1]/img'
    product3_hover_xpath = '//*[@id="homefeatured"]/li[3]/div/div[1]/div/a[1]/img'

    continue_shopping_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span'

    add1_to_cart = '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]'
    add2_to_cart = '//*[@id="homefeatured"]/li[1]/div/div[2]/div[2]/a[1]'
    add3_to_cart = '//*[@id="homefeatured"]/li[3]/div/div[2]/div[2]/a[1]'

    checkout_out_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'

    list_total_product_price_xpath = '//td[@class="cart_total"]/span'

    total_product = '//*[@id="total_product"]'

    proceed_checkout_xpath = '//*[@id="center_column"]/p[2]/a[1]'

    email_checkout_xpath = '//*[@id="email"]'

    pass_checkout_xpath = '//*[@id="passwd"]'

    button_signin_xpath = '//*[@id="SubmitLogin"]'

    # checkout after signIN
    proceed_checkout2_xpath = '//*[@id="center_column"]/form/p/button'

    click_term_xpath = '//*[@id="cgv"]'

    # check after Shipping
    proceed_checkout3_xpath = '//*[@id="form"]/p/button'

    payment_method = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'

    confirm_order_xpath = '//*[@id="cart_navigation"]/button'

    notice_order_success = '//div//*[@id="center_column"]/div/p/strong'

    # test change Order Detail

    product4_hover_xpath = '//*[@id="homefeatured"]/li[4]/div/div[1]/div/a[1]/img'
    product5_hover_xpath = '//*[@id="homefeatured"]/li[5]/div/div[1]/div/a[1]/img'

    add4_to_cart = '//*[@id="homefeatured"]/li[4]/div/div[2]/div[2]/a[1]'
    add5_to_cart = '//*[@id="homefeatured"]/li[5]/div/div[2]/div[2]/a[1]'

    random_product_xpath = '//input[@class="cart_quantity_input form-control grey"]'
    random_delete_xpath = '//i[@class="icon-trash"]'

    alert_term_xpath = '//*[@id="order"]/div[2]/div/div/div/div/p'
    close_alert_term = '//*[@id="order"]/div[2]/div/div/a'

    # test_sale_product
    list_product_xpath = '//*[@id="homefeatured"]/li'
    sale_product_xpath = '//*[@id="homefeatured"]/li/div/div[2]/div[1]/span[3]'

    # check sale order
    button_addtoCart = '//*[@id="add_to_cart"]/button'
    proceed_checkout = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'

    def __init__(self, driver):
        self.driver = driver

    # Order success
    def click_continue_shopping(self):
        self.driver.find_element_by_xpath(self.continue_shopping_xpath).click()

    def click_checkout(self):
        self.driver.find_element_by_xpath(self.checkout_out_xpath).click()

    def hover_product1(self):
        product1 = self.driver.find_element_by_xpath(self.product1_hover_xpath)
        add_tocart = self.driver.find_element_by_xpath(self.add1_to_cart)
        actions = ActionChains(self.driver)
        actions.move_to_element(product1).move_to_element(
            add_tocart).click().perform()

    def hover_product2(self):
        product2 = self.driver.find_element_by_xpath(self.product2_hover_xpath)
        add_tocart2 = self.driver.find_element_by_xpath(self.add2_to_cart)
        actions = ActionChains(self.driver)
        actions.move_to_element(product2).move_to_element(
            add_tocart2).click().perform()

    def hover_product3(self):
        product3 = self.driver.find_element_by_xpath(self.product3_hover_xpath)
        add_cart = self.driver.find_element_by_xpath(self.add3_to_cart)
        actions = ActionChains(self.driver)
        actions.move_to_element(product3).move_to_element(
            add_cart).click().perform()

    def total_price(self):
        list_total_product_price = self.driver.find_elements_by_xpath(
            self.list_total_product_price_xpath)  # list elt
        list_price = []
        for elt in list_total_product_price:
            total_product_price = elt.text
            list_price.append(float(total_product_price[1:]))
        return sum(list_price)

    def amount_total_product(self):
        total_all_product = self.driver.find_element_by_xpath(
            self.total_product).text
        amount_total_product = float(total_all_product[1:])
        return amount_total_product

    def click_proceed_checkout(self):
        self.driver.find_element_by_xpath(self.proceed_checkout_xpath).click()

    def input_email(self, input_key):
        self.driver.find_element_by_xpath(
            self.email_checkout_xpath).send_keys(input_key)

    def input_pass(self, password):
        self.driver.find_element_by_xpath(
            self.pass_checkout_xpath).send_keys(password)

    def click_signIn(self):
        self.driver.find_element_by_xpath(self.button_signin_xpath).click()

    def click_proceed_checkout2(self):
        self.driver.find_element_by_xpath(self.proceed_checkout2_xpath).click()

    def click_checkterm(self):
        self.driver.find_element_by_xpath(self.click_term_xpath).click()

    def click_proceed_checkout3(self):
        self.driver.find_element_by_xpath(self.proceed_checkout3_xpath).click()

    def chose_payment_method(self):
        self.driver.find_element_by_xpath(self.payment_method).click()

    def click_confirm(self):
        self.driver.find_element_by_xpath(self.confirm_order_xpath).click()

    def check_notice_success(self):
        return self.driver.find_element_by_xpath(self.notice_order_success).text

    # Change order detail
    def hover_product4(self):
        product4 = self.driver.find_element_by_xpath(self.product4_hover_xpath)
        add_cart = self.driver.find_element_by_xpath(self.add4_to_cart)
        actions = ActionChains(self.driver)
        actions.move_to_element(product4).move_to_element(
            add_cart).click().perform()

    def hover_product5(self):
        product5 = self.driver.find_element_by_xpath(self.product5_hover_xpath)
        add_cart = self.driver.find_element_by_xpath(self.add5_to_cart)
        actions = ActionChains(self.driver)
        actions.move_to_element(product5).move_to_element(
            add_cart).click().perform()

    def get_random(self, list_deleted):
        num1 = random.randint(0, len(list_deleted))
        if num1 in list_deleted:
            self.get_random(list_deleted)
        else:
            return num1

    def choice_random(self, list_deleted, value):
        lst_product = self.driver.find_elements_by_xpath(
            self.random_product_xpath)
        num1 = self.get_random(list_deleted)
        quantity_product = lst_product[num1]
        quantity_product.clear()
        quantity_product.send_keys(value)

    def delete_random(self, list_deleted):
        lst_product = self.driver.find_elements_by_xpath(
            self.random_delete_xpath)
        num2 = self.get_random(list_deleted)
        del_product = lst_product[num2]
        del_product.click()

    def check_alert_term(self):
        return self.driver.find_element_by_xpath(self.alert_term_xpath).text

    # Order sale
    def check_sale_product(self):
        lst_product = self.driver.find_elements_by_xpath(
            self.list_product_xpath)
        return lst_product

    def add_toCart(self):
        self.driver.find_element_by_xpath(self.button_addtoCart).click()

    def checkout(self):
        self.driver.find_element_by_xpath(self.proceed_checkout).click()
