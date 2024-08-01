from data.globals.globalData import globalData
from data.home.functions import *

def test_book_successful(set_successful_book):
    response = requests.post(links.book, data=book_data.validData)
    assert response.status_code == status_codes.CREATED
    assert response.json().get(globalData.success) is True

def test_less_than_30_minutes():
    response = requests.post(links.book, data=book_data.lessThan30Minutes)
    assert response.status_code == status_codes.BAD_REQUEST
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == book_data.lessThan30Minutes["message"]

def test_taken_slot(set_taken_slot):
    response = requests.post(links.book, data=book_data.takenSlot)
    assert response.status_code == status_codes.CONFLICT
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == book_data.takenSlot["message"]

def test_overlapped(set_taken_slot):
    response = requests.post(links.book, data=book_data.overlapped)
    assert response.status_code == status_codes.CONFLICT
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == book_data.overlapped["message"]

def test_past_date():
    response = requests.post(links.book, data=book_data.pastDate)
    assert response.status_code == status_codes.BAD_REQUEST
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == book_data.pastDate["message"]

def test_past_time():
    response = requests.post(links.book, data=book_data.pastTime)
    assert response.status_code == status_codes.BAD_REQUEST
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == book_data.pastTime["message"]

def test_end_time_before_start_time():
    response = requests.post(links.book, data=book_data.endTimeBeforeStartTime)
    assert response.status_code == status_codes.BAD_REQUEST
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == book_data.endTimeBeforeStartTime["message"]