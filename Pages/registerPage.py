from selenium.webdriver.support.select import Select


class RegisterPage():

    def __init__(self,driver):
        self.driver = driver
        self.gender_select_mr = "id_gender1"
        self.first_name_textbox_id = "customer_firstname"
        self.last_name_textbox_id = "customer_lastname"
        self.pass_textbox_id = "passwd"
        self.birth_day_dropdown_id = "days"
        self.birth_month_dropdown_id = "months"
        self.birth_year_dropdown_id = "years"
        self.address_id = "address1"
        self.city_id = "city"
        self.state_dropdown_id = "id_state"
        self.postcode_textbox_id = "postcode"
        self.mobile_num_textbox_id = "phone_mobile"
        self.address_alias_textbox_id = "alias"
        self.reg_btn_id = "submitAccount"

    def select_gender(self):
        self.driver.find_element_by_id(self.gender_select_mr).click()

    def enter_first_name(self,fname):
        self.driver.find_element_by_id(self.first_name_textbox_id).clear()
        self.driver.find_element_by_id(self.first_name_textbox_id).send_keys(fname)

    def enter_last_name(self,lname):
        self.driver.find_element_by_id(self.last_name_textbox_id).clear()
        self.driver.find_element_by_id(self.last_name_textbox_id).send_keys(lname)

    def enter_pass(self,password):
        self.driver.find_element_by_id(self.pass_textbox_id).clear()
        self.driver.find_element_by_id(self.pass_textbox_id).send_keys(password)

    def select_birthday(self,day):
        select = Select(self.driver.find_element_by_id(self.birth_day_dropdown_id))
        select.select_by_index(day)

    def select_birth_month(self,month):
        select = Select(self.driver.find_element_by_id(self.birth_month_dropdown_id))
        select.select_by_index(month)

    def select_birth_year(self,age):
        select = Select(self.driver.find_element_by_id(self.birth_year_dropdown_id))
        select.select_by_index(age)

    def enter_address(self, address):
        self.driver.find_element_by_id(self.address_id).clear()
        self.driver.find_element_by_id(self.address_id).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element_by_id(self.city_id).clear()
        self.driver.find_element_by_id(self.city_id).send_keys(city)

    def select_state(self,state):
        select = Select(self.driver.find_element_by_id(self.state_dropdown_id))
        select.select_by_index(state)

    def enter_postcode(self,postcode):
        self.driver.find_element_by_id(self.postcode_textbox_id).clear()
        self.driver.find_element_by_id(self.postcode_textbox_id).send_keys(postcode)

    def enter_mobile_num(self, mobile):
        self.driver.find_element_by_id(self.mobile_num_textbox_id).clear()
        self.driver.find_element_by_id(self.mobile_num_textbox_id).send_keys(mobile)

    def enter_address_alias(self, address):
        self.driver.find_element_by_id(self.address_alias_textbox_id).clear()
        self.driver.find_element_by_id(self.address_alias_textbox_id).send_keys(address)

    def click_create_acc(self):
        self.driver.find_element_by_id(self.reg_btn_id).click()
