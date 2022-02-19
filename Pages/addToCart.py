from selenium.webdriver import ActionChains
from time import sleep



class AddToCart():

    def __init__(self, driver):
        self.driver = driver
        self.casual_dress = "//*[@class='product_list grid row']/li"
        self.casual_dress_addtocart_btn ="//*[@title='Add to cart']"
        self.checkout_cart_btn ="//*[@title='Proceed to checkout']"
        self.continue_shopping_btn = "//*[@title='Continue shopping']"
        self.tshirt_page_btn = "#block_top_menu > ul > li:nth-child(3)"
        self.tshirt_addtocart_btn = "//*[@title='Add to cart']"
        self.tshirt_card = "//*[@class='product_list grid row']/li"

    def add_causal_dress_to_cart(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath(self.casual_dress)).perform()
        self.driver.find_element_by_xpath(self.casual_dress_addtocart_btn).click()
        self.driver.implicitly_wait(5)

    def click_continue_shoppingt(self):
        self.driver.find_element_by_xpath(self.continue_shopping_btn).click()
        self.driver.implicitly_wait(10)

    def add_tshirt_to_cart(self):
        self.driver.find_element_by_css_selector(self.tshirt_page_btn).click()
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath(self.tshirt_card)).perform()
        self.driver.find_element_by_xpath(self.tshirt_addtocart_btn).click()
        self.driver.implicitly_wait(5)

    def checkout_cart(self):
        self.driver.find_element_by_xpath(self.checkout_cart_btn).click()
        sleep(2)
