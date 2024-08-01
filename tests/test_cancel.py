import time

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataAndFunctions.home.functions import set_invalid_book
from dataAndFunctions.home.cancel_data import cancel_data
from dataAndFunctions.home.home_setup import Setup

set = Setup(driver=Setup.driver)

def test_successful_cancel(set_invalid_book):
    set.enter_date(cancel_data.successfulCancel["date"])
    set.enter_start_time(cancel_data.successfulCancel["start_time"])
    set.enter_end_time(cancel_data.successfulCancel["end_time"])
    set.click_book_button()
    set.click_cancel_button()
    # time.sleep(2)
    assert set.return_taos_message() == cancel_data.successfulCancel["message"]

def test_appointment_not_exists(set_invalid_book):
    set.enter_date(cancel_data.appointmentNotExists["date"])
    set.enter_start_time(cancel_data.appointmentNotExists["start_time"])
    set.enter_end_time(cancel_data.appointmentNotExists["end_time"])
    set.click_cancel_button()
    # time.sleep(1)
    assert set.return_taos_message() == cancel_data.appointmentNotExists["message"]

# def test():
#     set.driver.quit()


