import time
import pytest
from dataAndFunctions.home.home_setup import Setup
from dataAndFunctions.links import links
from dataAndFunctions.home.book_data import book_data
from dataAndFunctions.globalData import globalData

@pytest.fixture
def set_valid_book():
    set = Setup(driver=Setup.driver)
    set.enter_username(globalData.data["username"])
    set.enter_password(globalData.data["password"])
    set.enter_phone(globalData.data["phone"])
    set.click_button()
    set.enter_username_login(globalData.data["username"])
    set.enter_password_login(globalData.data["password"])
    set.click_login()
    yield set
    set.click_cancel_button()
    # time.sleep(1)
    set.driver.get(links.link)

@pytest.fixture
def set_invalid_book():
    set = Setup(driver=Setup.driver)
    time.sleep(1)
    set.enter_username(globalData.data["username"])
    set.enter_password(globalData.data["password"])
    set.enter_phone(globalData.data["phone"])
    set.click_button()
    set.enter_username_login(globalData.data["username"])
    set.enter_password_login(globalData.data["password"])
    set.click_login()
    yield set
    # time.sleep(1)
    set.driver.get(links.link)

@pytest.fixture
def set_taken_slot():
    set = Setup(driver=Setup.driver)
    set.enter_username(globalData.data["username"])
    set.enter_password(globalData.data["password"])
    set.enter_phone(globalData.data["phone"])
    set.click_button()
    set.enter_username_login(globalData.data["username"])
    set.enter_password_login(globalData.data["password"])
    set.click_login()
    set.enter_date(book_data.takenSlot["date"])
    set.enter_start_time(book_data.takenSlot["start_time"])
    set.enter_end_time(book_data.takenSlot["end_time"])
    set.click_book_button()
    yield set
    set.click_cancel_button()
    set.driver.get(links.link)

@pytest.fixture
def set_overlapped_appointment():
    set = Setup(driver=Setup.driver)
    set.enter_username(globalData.data["username"])
    set.enter_password(globalData.data["password"])
    set.enter_phone(globalData.data["phone"])
    set.click_button()
    set.enter_username_login(globalData.data["username"])
    set.enter_password_login(globalData.data["password"])
    set.click_login()
    set.enter_date(book_data.takenSlot["date"])
    set.enter_start_time(book_data.takenSlot["start_time"])
    set.enter_end_time(book_data.takenSlot["end_time"])
    set.click_book_button()
    yield set
    set.enter_date(book_data.takenSlot["date"])
    set.enter_start_time(book_data.takenSlot["start_time"])
    set.enter_end_time(book_data.takenSlot["end_time"])
    set.click_cancel_button()
    set.driver.get(links.link)
