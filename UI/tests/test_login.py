import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataAndFunctions.index.functions import set_login_valid
from dataAndFunctions.index.login_data import login_data
import time
from dataAndFunctions.index.index_setup import Setup
from dataAndFunctions.links import links

set = Setup(driver=Setup.driver)

def test_valid(set_login_valid):
    set.enter_username_login(login_data.validData["username"])
    set.enter_password_login(login_data.validData["password"])
    set.click_login()
    time.sleep(1)
    assert set.return_taos_message() == login_data.validData["message"]
    set.driver.get(links.link)

def test_wrong_username():
    set.enter_username_login(login_data.wrongUsername["username"])
    set.enter_password_login(login_data.wrongUsername["password"])
    set.click_login()
    assert set.return_taos_message() == login_data.wrongUsername["message"]

def test_wrong_password():
    set.enter_username_login(login_data.wrongPassword["username"])
    set.enter_password_login(login_data.wrongPassword["password"])
    set.click_login()
    assert set.return_taos_message() == login_data.wrongPassword["message"]

def test_empty_username():
    set.driver.get(links.link)
    set.enter_password_login(login_data.validData["password"])
    set.click_login()
    assert set.return_taos_message() == login_data.emptyFields
    set.login_cleanUp()

def test_empty_password():
    set.enter_username_login(login_data.validData["username"])
    set.click_login()
    assert set.return_taos_message() == login_data.emptyFields
    set.login_cleanUp()

def test_empty():
    set.click_login()
    assert set.return_taos_message() == login_data.emptyFields

def test():
    set.driver.quit()
