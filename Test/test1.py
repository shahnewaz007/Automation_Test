from selenium import webdriver
import time
import unittest
from faker import Faker
from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from Pages.registerPage import RegisterPage
from Pages.myaccountPage import MyAccountPage
from Pages.addToCart import AddToCart
from Pages.checkoutPage import CheckoutPage


class AutomationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="F:\Education\Job\Brain Station\TestAutomation\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_Automation(self):
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")

        click_signin_obj = HomePage(driver)
        login_page_obj = LoginPage(driver)
        MyAccountPage_obj = MyAccountPage(driver)
        addToCart_obj = AddToCart(driver)
        checkoutPage_obj = CheckoutPage(driver)

        def login(email):
            login_page_obj.enter_email(email)
            login_page_obj.enter_pass("123456")
            login_page_obj.click_signin()

        click_signin_obj.click_signin()
        fake = Faker()
        email_list = [fake.ascii_email(),fake.ascii_email()]

        # ====================================== Registration ==========================================================


        #Create First Account
        login_page_obj.enter_reg_email(email_list[0])
        login_page_obj.click_create_acc()

        reg_Page_obj = RegisterPage(driver)
        reg_Page_obj.select_gender()
        reg_Page_obj.enter_first_name("Ayon")
        reg_Page_obj.enter_last_name("Mahmud")
        reg_Page_obj.enter_pass("123456")
        reg_Page_obj.select_birthday(23)
        reg_Page_obj.select_birth_month(9)
        reg_Page_obj.select_birth_year(24)
        reg_Page_obj.enter_address("Road 24/2, California")
        reg_Page_obj.enter_city("New York")
        reg_Page_obj.select_state(5)
        reg_Page_obj.enter_postcode(90011)
        reg_Page_obj.enter_mobile_num(1785499256)
        reg_Page_obj.enter_address_alias("Road 24/2, California")
        reg_Page_obj.click_create_acc()

        time.sleep(3)
        MyAccountPage_obj.click_signout()


        # Create Second Account
        login_page_obj.enter_reg_email(email_list[1])
        login_page_obj.click_create_acc()

        reg_Page_obj = RegisterPage(driver)
        reg_Page_obj.select_gender()
        reg_Page_obj.enter_first_name("Abdur")
        reg_Page_obj.enter_last_name("Rahman")
        reg_Page_obj.enter_pass("123456")
        reg_Page_obj.select_birthday(22)
        reg_Page_obj.select_birth_month(10)
        reg_Page_obj.select_birth_year(26)
        reg_Page_obj.enter_address("Road 24/2, California")
        reg_Page_obj.enter_city("New York")
        reg_Page_obj.select_state(5)
        reg_Page_obj.enter_postcode(90011)
        reg_Page_obj.enter_mobile_num(1785499256)
        reg_Page_obj.enter_address_alias("Road 24/2, California")
        reg_Page_obj.click_create_acc()

        time.sleep(3)
        MyAccountPage_obj.click_signout()


        # ====================================== Login & Shopping ==========================================================


        for email in email_list:
            login(email)
            MyAccountPage_obj.click_casual_dress()
            addToCart_obj.add_causal_dress_to_cart()
            addToCart_obj.click_continue_shoppingt()
            addToCart_obj.add_tshirt_to_cart()
            addToCart_obj.checkout_cart()

            checkoutPage_obj.click_summery_proceed_to_checkout()
            checkoutPage_obj.click_address_proceed_to_checkout()
            checkoutPage_obj.click_shipping_proceed_to_checkout()
            checkoutPage_obj.payment()

            MyAccountPage_obj.click_signout()
