import pytest
from data.index.signUp_data import signUpData
from data.globals.links import links
import requests

@pytest.fixture
def set_taken():
    requests.post(links.signup, json=signUpData.validSignUpData)
