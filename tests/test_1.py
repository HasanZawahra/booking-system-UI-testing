import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time

from dataAndFunctions.links import links
from dataAndFunctions.index.functions import *
from dataAndFunctions.index.signUp_data import signUpData
from dataAndFunctions.index.index_setup import Setup

set = Setup(driver=Setup.driver)

def test_valid():
    set.enter_username(signUpData.validSignUpData["username"])
    set.enter_password(signUpData.validSignUpData["password"])
    set.enter_phone(signUpData.validSignUpData["phone"])
    set.click_button()
    assert set.return_taos_message() == signUpData.validSignUpData["message"]
    set.cleanUp()

def test_existing_username():
    set.enter_username(signUpData.existingUserName["username"])
    set.enter_password(signUpData.existingUserName["password"])
    set.enter_phone(signUpData.existingUserName["phone"])
    set.click_button()
    assert set.return_taos_message() == signUpData.existingUserName["message"]
    set.cleanUp()

def test_phone_number_username():
    set.enter_username(signUpData.existingPhoneNumber["username"])
    set.enter_password(signUpData.existingPhoneNumber["password"])
    set.enter_phone(signUpData.existingPhoneNumber["phone"])
    set.click_button()
    assert set.return_taos_message() == signUpData.existingPhoneNumber["message"]
    set.cleanUp()


def test_both_exist():
    set.enter_username(signUpData.bothExist["username"])
    set.enter_password(signUpData.bothExist["password"])
    set.enter_phone(signUpData.bothExist["phone"])
    set.click_button()
    assert (set.return_taos_message() == signUpData.bothExist["message"])
    set.cleanUp()


def test_empty_username():
    set.driver.get(links.link)
    time.sleep(1)
    set.enter_password(signUpData.validSignUpData["password"])
    set.enter_phone(signUpData.validSignUpData["phone"])
    set.click_button()
    assert (set.return_taos_message() == signUpData.emptyFields)
    set.cleanUp()

def test_empty_password():
    set.enter_username(signUpData.validSignUpData["username"])
    set.enter_phone(signUpData.validSignUpData["phone"])
    set.click_button()
    assert set.return_taos_message() == signUpData.emptyFields
    set.cleanUp()

def test_empty_phone():
    set.enter_username(signUpData.validSignUpData["username"])
    set.enter_password(signUpData.validSignUpData["password"])
    set.click_button()
    assert set.return_taos_message() == signUpData.emptyFields
    set.cleanUp()

def test_empty_all():
    set.click_button()
    assert set.return_taos_message() == signUpData.emptyFields
    set.cleanUp()

# def test_close():
#     set.driver.quit()