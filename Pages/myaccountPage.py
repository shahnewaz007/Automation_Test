from selenium.webdriver import ActionChains

class MyAccountPage():

    def __init__(self,driver):
        self.driver = driver
        self.signOut_btn_name = "logout"

    def click_signout(self):
        self.driver.find_element_by_class_name(self.signOut_btn_name).click()

    def click_casual_dress(self):
        action = ActionChains(self.driver)
        action.move_to_element(
            self.driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-child(2)")).perform()
        self.driver.find_element_by_css_selector(
            "#block_top_menu > ul > li:nth-child(2) > ul > li:nth-child(1) > a").click()
