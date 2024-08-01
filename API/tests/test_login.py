from data.globals.status_codes import status_codes
from data.globals.links import links
from data.globals.globalData import globalData
import requests
from data.index.login_data import login_data
from data.index.functions import *

def test_login_successful(set_taken):
    response = requests.post(links.login, json=login_data.validData)
    assert response.status_code == status_codes.OK
    assert response.json().get(globalData.success) is True

def test_wrong_username():
    response = requests.post(links.login, json=login_data.wrongUsername)
    assert response.status_code == status_codes.UNAUTHORIZED
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == login_data.wrongUsername['message']

def test_wrong_password():
    response = requests.post(links.login, json=login_data.wrongPassword)
    assert response.status_code == status_codes.UNAUTHORIZED
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == login_data.wrongPassword['message']

def test_both_wrong():
    response = requests.post(links.login, json=login_data.bothAreWrong)
    assert response.status_code == status_codes.UNAUTHORIZED
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == login_data.bothAreWrong['message']