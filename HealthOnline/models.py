from django.db import models
from django.contrib.auth.models import User

# Create your models

class Department(models.Model):
    title = models.CharField(max_length=100)


class Specialization(models.Model):
    name = models.CharField(max_length=100)


class Room(models.Model):
    room_number = models.IntegerField(max_length=3)
    room_floor = models.IntegerField(max_length=2)


class Doctor(models.Model):
    gender = [('M', 'Male'), ('F', 'Female')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(choices=gender)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)


class Patient(models.Model):
    gender = [('M', 'Male'), ('F', 'Female')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(choices=gender)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)


class PaymentType(models.Model):
    types = [('Cash', 'Cash'), ('Online', 'Online')]

    title = models.CharField(choices=types)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.DateField()
    is_visit = models.BooleanField(default=False)


class Visits(models.Model):
    date = models.DateField()
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)


class Payment(models.Model):
    visit = models.ForeignKey(Visits, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    is_paid = models.BooleanField(default=False)
