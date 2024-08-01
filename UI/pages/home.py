from selenium.webdriver.common.by import By
from .common import Common

class home(Common):

    locators = {
        "DATE" : (By.ID, 'date'),
        "START_TIME" : (By.ID, 'start-time'),
        "END_TIME" : (By.ID, 'end-time'),
        "BOOK_BUTTON" : (By.XPATH, '//*[@id="booking-form"]/button'),
        "CANCEL_BUTTON" : (By.XPATH, '//*[@id="cancel-appointment"]'),
        "SIGNUP_USERNAME": (By.ID, 'signup-username'),
        "SIGNUP_PASSWORD": (By.ID, 'signup-password'),
        "SIGNUP_PHONE": (By.ID, 'signup-phone'),
        "SIGNUP_BUTTON": (By.XPATH, '//*[@id="signup-form"]/button'),
        "MESSAGE": (By.ID, 'message'),
        "LOGIN_USERNAME": (By.ID, 'login-username'),
        "LOGIN_PASSWORD": (By.ID, 'login-password'),
        "LOGIN_BUTTON": (By.XPATH, '//*[@id="login-form"]/button')
    }

    def enter_date(self, date):
        self.wait_for(self.locators["DATE"]).send_keys(date)

    def enter_start_time(self, start_time):
        self.wait_for(self.locators["START_TIME"]).send_keys(start_time)

    def enter_end_time(self, end_time):
        self.wait_for(self.locators["END_TIME"]).send_keys(end_time)

    def click_book_button(self):
        self.find(self.locators["BOOK_BUTTON"]).click()

    def click_cancel_button(self):
        self.find(self.locators["CANCEL_BUTTON"]).click()

    def return_taos_message(self):
        return self.wait_for(self.locators["MESSAGE"]).text

    def cleanUpDate(self):
        self.wait_for(self.locators["DATE"]).clear()
        self.wait_for(self.locators["START_TIME"]).clear()
        self.wait_for(self.locators["END_TIME"]).clear()

    def enter_username(self, username):
        self.wait_for(self.locators["SIGNUP_USERNAME"]).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.locators["SIGNUP_PASSWORD"]).send_keys(password)

    def enter_phone(self, phone):
        self.wait_for(self.locators["SIGNUP_PHONE"]).send_keys(phone)

    def click_button(self):
        self.find(self.locators["SIGNUP_BUTTON"]).click()


    def cleanUpAuth(self):
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