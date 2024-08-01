from data.globals.globalData import globalData
from data.globals.status_codes import status_codes
from data.index.functions import *

def test_signup_successful():
    response = requests.post(links.signup, json=signUpData.validSignUpData)
    assert response.status_code == status_codes.CREATED
    assert response.json().get(globalData.success) is True

def test_taken_username(set_taken):
    response = requests.post(links.signup, json=signUpData.existingUserName)
    assert response.status_code == status_codes.CONFLICT
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == signUpData.existingUserName['message']

def test_taken_phone_number(set_taken):
    response = requests.post(links.signup, json=signUpData.existingPhoneNumber)
    assert response.status_code == status_codes.CONFLICT
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == signUpData.existingPhoneNumber['message']

def test_both_taken(set_taken):
    response = requests.post(links.signup, json=signUpData.bothExist)
    assert response.status_code == status_codes.CONFLICT
    assert response.json().get(globalData.success) is False
    assert response.json().get(globalData.message) == signUpData.bothExist['message']