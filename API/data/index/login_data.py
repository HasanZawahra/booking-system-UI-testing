from data.globals.globalData import globalData

class login_data:
    validData = {
        "username" : globalData.data["username"],
        "password" : globalData.data["password"],
        "message" : "Logged in successfully"
    }

    wrongUsername = {
        "username" : "hasn",
        "password" : globalData.data["password"],
        "message" : "Invalid username or password"
    }

    wrongPassword = {
        "username" : globalData.data["username"],
        "password" : "1234",
        "message" : "Invalid username or password"
    }

    bothAreWrong = {
        "username" : "hasn",
        "password" : "1234",
        "message" : "Invalid username or password"
    }