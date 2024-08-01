from data.globals.globalData import globalData

class cancel_data:

    successfulCancel = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "15:00",
        "endTime": "15:30"
    }

    appointmentNotExists = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "15:00",
        "endTime": "15:30",
        "message": "No appointment found to cancel"
    }