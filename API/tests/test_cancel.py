from data.globals.globalData import globalData
from data.home.functions import *

def test_successful_cancel(set_cancel):
    response = requests.post(links.cancel, data=cancel_data.successfulCancel)
    assert response.status_code == status_codes.OK
    assert response.json().get(globalData.success) is True

def test_cancel_not_exists():
    response = requests.post(links.cancel, data=cancel_data.appointmentNotExists)
    assert response.status_code == status_codes.NOT_FOUND
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == cancel_data.appointmentNotExists["message"]