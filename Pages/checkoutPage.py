class CheckoutPage():

    def __init__(self,driver):
        self.driver = driver
        self.summery_proceed_btn = "//*[@class='cart_navigation clearfix']/a"
        self.address_proceed_btn = "//*[@name='processAddress']"
        self.tos_checkbox_id = "cgv"
        self.shipping_proceed_btn_name = "processCarrier"
        self.payment_pay_by_check_btn = "//*[@title='Pay by check.']"
        self.confirm_order_btn = "//*[@class='button btn btn-default button-medium']"

    def click_summery_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.summery_proceed_btn).click()

    def click_address_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.address_proceed_btn).click()

    def click_shipping_proceed_to_checkout(self):
        self.driver.find_element_by_id(self.tos_checkbox_id).click()
        self.driver.find_element_by_name(self.shipping_proceed_btn_name).click()

    def payment(self):
        self.driver.find_element_by_xpath(self.payment_pay_by_check_btn).click()
        self.driver.find_element_by_xpath(self.confirm_order_btn).click()
        self.driver.implicitly_wait(5)
