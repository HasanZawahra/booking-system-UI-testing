class book_data:

    emptyMessage = "Logged in successfully"

    validData = {
        "date": "12-11-2024",
        "start_time": "09-00PM",
        "end_time": "09-30PM",
        "message": "Appointment booked successfully"
    }

    lessThan30Minutes = {
        "date": "10-10-2024",
        "start_time": "10-00PM",
        "end_time": "10-25PM",
        "message": "Appointment must be at least 30 minutes"
    }

    takenSlot = {
        "date": "10-10-2024",
        "start_time": "11-00PM",
        "end_time": "11-30PM",
        "message": "Appointment slot already booked or overlaps with another appointment"
    }

    overlapped = {
        "date": "10-10-2024",
        "start_time": "10-40PM",
        "end_time": "11-15PM",
        "message": "Appointment slot already booked or overlaps with another appointment"
    }

    pastDate = {
        "date": "10-10-2021",
        "start_time": "09-00PM",
        "end_time": "09-30PM",
        "message": "Cannot book an appointment in the past"
    }

    pastTime = {
        "date": "07-29-2024",
        "start_time": "09-00AM",
        "end_time": "09-30AM",
        "message": "Cannot book an appointment in the past"
    }

    endTimeBeforeStartTime = {
        "date": "10-10-2024",
        "start_time": "09-00PM",
        "end_time": "08-30PM",
        "message": "Appointment must be at least 30 minutes"
    }
