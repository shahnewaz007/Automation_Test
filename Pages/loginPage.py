class LoginPage():

    def __init__(self,driver):
        self.driver = driver
        self.email_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.signin_btn_id = "SubmitLogin"
        self.reg_email_textbox_id = "email_create"
        self.create_acc_btn_id = "SubmitCreate"


    def enter_email(self,email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_pass(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_signin(self):
        self.driver.find_element_by_id(self.signin_btn_id).click()

    def enter_reg_email(self,email):
        self.driver.find_element_by_id(self.reg_email_textbox_id).clear()
        self.driver.find_element_by_id(self.reg_email_textbox_id).send_keys(email)

    def click_create_acc(self):
        self.driver.find_element_by_id(self.create_acc_btn_id).click()
