import pytest
from dataAndFunctions.index.index_setup import Setup
from dataAndFunctions.globalData import globalData


@pytest.fixture
def set_login_valid():
    set = Setup(driver=Setup.driver)
    set.enter_username(globalData.data["username"])
    set.enter_password(globalData.data["password"])
    set.enter_phone(globalData.data["phone"])
    set.click_button()