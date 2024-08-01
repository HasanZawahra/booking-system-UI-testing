import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataAndFunctions.home.functions import set_invalid_book, set_valid_book, set_taken_slot, set_overlapped_appointment
from dataAndFunctions.home.book_data import book_data
from dataAndFunctions.home.home_setup import Setup


set = Setup(driver=Setup.driver)

def test_valid(set_valid_book):
    set.enter_date(book_data.validData["date"])
    set.enter_start_time(book_data.validData["start_time"])
    set.enter_end_time(book_data.validData["end_time"])
    set.click_book_button()
    assert set.return_taos_message() == book_data.validData["message"]

def test_taken_slot(set_taken_slot):
    set_taken_slot.enter_date(book_data.takenSlot["date"])
    set_taken_slot.enter_start_time(book_data.takenSlot["start_time"])
    set_taken_slot.enter_end_time(book_data.takenSlot["end_time"])
    set_taken_slot.click_book_button()
    assert set_taken_slot.return_taos_message() == book_data.takenSlot["message"]

def test_less_than_30_minutes(set_invalid_book):
    set.enter_date(book_data.lessThan30Minutes["date"])
    set.enter_start_time(book_data.lessThan30Minutes["start_time"])
    set.enter_end_time(book_data.lessThan30Minutes["end_time"])
    set.click_book_button()
    assert set.return_taos_message() == book_data.lessThan30Minutes["message"]

def test_overlapped(set_overlapped_appointment):
    set.enter_date(book_data.overlapped["date"])
    set.enter_start_time(book_data.overlapped["start_time"])
    set.enter_end_time(book_data.overlapped["end_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.overlapped["message"]

def test_past_date(set_invalid_book):
    set.enter_date(book_data.pastDate["date"])
    set.enter_start_time(book_data.pastDate["start_time"])
    set.enter_end_time(book_data.pastDate["end_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.pastDate["message"]
#
def test_past_time(set_invalid_book):
    set.enter_date(book_data.pastTime["date"])
    set.enter_start_time(book_data.pastTime["start_time"])
    set.enter_end_time(book_data.pastTime["end_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.pastTime["message"]

def test_end_time_before_start_time(set_invalid_book):
    set.enter_date(book_data.endTimeBeforeStartTime["date"])
    set.enter_start_time(book_data.endTimeBeforeStartTime["start_time"])
    set.enter_end_time(book_data.endTimeBeforeStartTime["end_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.endTimeBeforeStartTime["message"]

def test_empty_date(set_invalid_book):
    set.enter_date(book_data.emptyMessage)
    set.enter_start_time(book_data.validData["start_time"])
    set.enter_end_time(book_data.validData["end_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.emptyMessage

def test_empty_start_time(set_invalid_book):
    set.enter_date(book_data.validData["date"])
    set.enter_end_time(book_data.validData["end_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.emptyMessage

def test_empty_end_time(set_invalid_book):
    set.enter_date(book_data.validData["date"])
    set.enter_start_time(book_data.validData["start_time"])
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.emptyMessage

def test_Allempty(set_invalid_book):
    set.click_book_button()
    # time.sleep(1)
    assert set.return_taos_message() == book_data.emptyMessage

# def test():
#     set.driver.quit()