class signUpData:

    validSignUpData = {
        "username": "hasan",
        "password": "123",
        "phone": "123",
        "message": "Account created successfully. Please login."
    }

    existingUserName = {
        "username": validSignUpData["username"],
        "password": "123",
        "phone": "111",
        "message": "Username or phone number already exists"
    }

    existingPhoneNumber = {
        "username": "george",
        "password": "123",
        "phone": validSignUpData["phone"],
        "message": "Username or phone number already exists"
    }

    bothExist = {
        "username": validSignUpData["username"],
        "password": "123",
        "phone": validSignUpData["phone"],
        "message": "Username or phone number already exists"
    }

    emptyFields = ""