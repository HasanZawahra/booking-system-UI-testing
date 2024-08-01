from data.home.book_data import book_data
import pytest
from data.globals.links import links
import requests
from data.home.cancel_data import cancel_data
from data.globals.status_codes import status_codes

@pytest.fixture
def set_successful_book():
    yield
    response = requests.post(links.cancel, data=book_data.validData)
    assert response.status_code == status_codes.OK

@pytest.fixture
def set_taken_slot():
    response = requests.post(links.book, data=book_data.takenSlot)
    assert response.status_code == status_codes.CREATED
    yield
    response = requests.post(links.cancel, data=book_data.takenSlot)
    assert response.status_code == status_codes.OK


@pytest.fixture
def set_cancel():
    response = requests.post(links.book, data=cancel_data.successfulCancel)
    assert response.status_code == status_codes.CREATED
