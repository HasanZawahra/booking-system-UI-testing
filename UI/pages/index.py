from selenium.webdriver.common.by import By
from .common import Common

class index(Common):

    locators = {
        "SIGNUP_USERNAME" : (By.ID, 'signup-username'),
        "SIGNUP_PASSWORD" : (By.ID, 'signup-password'),
        "SIGNUP_PHONE" : (By.ID, 'signup-phone'),
        "SIGNUP_BUTTON" : (By.XPATH, '//*[@id="signup-form"]/button'),
        "MESSAGE" : (By.ID, 'message'),
        "LOGIN_USERNAME" : (By.ID, 'login-username'),
        "LOGIN_PASSWORD" : (By.ID, 'login-password'),
        "LOGIN_BUTTON" : (By.XPATH, '//*[@id="login-form"]/button')
    }

    def enter_username(self, username):
        self.find(self.locators["SIGNUP_USERNAME"]).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.locators["SIGNUP_PASSWORD"]).send_keys(password)

    def enter_phone(self, phone):
        self.wait_for(self.locators["SIGNUP_PHONE"]).send_keys(phone)

    def click_button(self):
        self.find(self.locators["SIGNUP_BUTTON"]).click()

    def return_taos_message(self):
        return self.wait_for(self.locators["MESSAGE"]).text

    def cleanUp(self):
        self.wait_for(self.locators["SIGNUP_USERNAME"]).clear()
        self.wait_for(self.locators["SIGNUP_PASSWORD"]).clear()
        self.wait_for(self.locators["SIGNUP_PHONE"]).clear()

    def enter_username_login(self, username):
        self.wait_for(self.locators["LOGIN_USERNAME"]).send_keys(username)

    def enter_password_login(self, password):
        self.wait_for(self.locators["LOGIN_PASSWORD"]).send_keys(password)

    def click_login(self):
        self.find(self.locators["LOGIN_BUTTON"]).click()

    def login_cleanUp(self):
        self.wait_for(self.locators["LOGIN_USERNAME"]).clear()
        self.wait_for(self.locators["LOGIN_PASSWORD"]).clear()