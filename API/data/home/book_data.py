from data.globals.globalData import globalData
class book_data:
    validData = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "15:00",
        "endTime": "15:30"
    }

    lessThan30Minutes = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "15:00",
        "endTime": "15:25",
        "message": "Appointment must be at least 30 minutes"
    }

    takenSlot = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "15:00",
        "endTime": "15:30",
        "message": "Appointment slot already booked or overlaps with another appointment"
    }

    overlapped = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "14:50",
        "endTime": "15:25",
        "message": "Appointment slot already booked or overlaps with another appointment"
    }

    pastDate = {
        "username": globalData.data["username"],
        "date": "2023-11-12",
        "startTime": "14:50",
        "endTime": "15:25",
        "message": "Cannot book an appointment in the past"
    }

    pastTime = {
        "username": globalData.data["username"],
        "date": "2024-30-07",
        "startTime": "11:50",
        "endTime": "12:25",
        "message": "Cannot book an appointment in the past"
    }

    endTimeBeforeStartTime = {
        "username": globalData.data["username"],
        "date": "2024-11-12",
        "startTime": "15:50",
        "endTime": "14:25",
        "message": "Appointment must be at least 30 minutes"
    }