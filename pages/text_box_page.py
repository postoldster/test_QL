import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class TextBoxPage(BasePage):

    PAGE_URL = Links.TEXT_BOX

    FULLNAME_FIELD = ("id", "userName")  #("xpath", "//input[@id='userName']")
    USER_EMAIL_FIELD = ("id", "userEmail")
    CURRENT_ADDRESS_FIELD = ("id", "currentAddress")
    PERMANENT_ADDRESS_FIELD = ("id", "permanentAddress")
    SUBMIT_BUTTON = ("id", "submit")
    OUTPUT = ("xpath", "//div[@id='output']/div/p")
    OUTPUT_FULLNAME = ("xpath", "//p[@id='name']")
    OUTPUT_USER_EMAIL = ("xpath", "//p[@id='email']")
    OUTPUT_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")

    @allure.step("Enter full name")
    def enter_fullname(self, fullname: str):
        self.wait.until(EC.element_to_be_clickable(self.FULLNAME_FIELD)).send_keys(fullname)

    @allure.step("Enter user email")
    def enter_user_email(self, user_email):
        self.wait.until(EC.element_to_be_clickable(self.USER_EMAIL_FIELD)).send_keys(user_email)

    @allure.step("Enter current address")
    def enter_current_address(self, address):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS_FIELD)).send_keys(address)

    @allure.step("Enter permanent address")
    def enter_permanent_address(self, address):
        self.wait.until(EC.element_to_be_clickable(self.PERMANENT_ADDRESS_FIELD)).send_keys(address)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.presence_of_element_located(self.SUBMIT_BUTTON)).location_once_scrolled_into_view
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Check output after submitting form")
    def check_output(self, data):
        self.wait.until(EC.visibility_of_element_located(self.OUTPUT))
        self.wait.until(EC.text_to_be_present_in_element(self.OUTPUT_FULLNAME, data["full_name"]))
        self.wait.until(EC.text_to_be_present_in_element(self.OUTPUT_USER_EMAIL, data["user_email"]))
        self.wait.until(EC.text_to_be_present_in_element(self.OUTPUT_CURRENT_ADDRESS, data["current_address"]))
        self.wait.until(EC.text_to_be_present_in_element(self.OUTPUT_PERMANENT_ADDRESS, data["permanent_address"]))