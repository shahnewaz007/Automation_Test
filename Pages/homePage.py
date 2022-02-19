class HomePage():

    def __init__(self,driver):
        self.driver = driver
        self.signIn_btn_name = "login"

    def click_signin(self):
        self.driver.find_element_by_class_name(self.signIn_btn_name).click()
