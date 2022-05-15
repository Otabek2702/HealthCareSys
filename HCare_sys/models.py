class Patient:
    def __init__(self, f_name, l_name, age, gender, address, phone_number, register_date, last_visit):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.register_date = register_date
        self.last_visit = last_visit


class Doctor:
    def __init__(self, f_name, l_name, age, gender, address, phone_number, specialization_id, room_id, registered_date):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.specialization_id = specialization_id
        self.room_id = room_id
        self.registered_date = registered_date


class Payment:
    def __init__(self):
        pass


class Specialization:
    def __init__(self, id):
        self.id = id


class Visits:
    def __init__(self):
        pass


class Appointment:
    def __init__(self):
        pass


class Room:
    def __init__(self):
        pass
