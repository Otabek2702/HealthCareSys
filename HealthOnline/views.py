from django.shortcuts import render
from django.views import View

# from .models import User, Room, Patient, Visits, Payment, PaymentType, Doctor, Appointment, Department, Specialization

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'onlineView/index.html')
