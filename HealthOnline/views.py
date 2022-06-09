from django.shortcuts import render
from django.views import View

from .models import User, Room, Patient, Visits, Payment, PaymentType, Doctor, Appointment, Department, Specialization

# Create your views here.


class IndexView(View):
    def get(self, request):
        context = {'department': Department.objects.all()}
        return render(request, "onlineView/index.html", context=context)

    def post(self, request):
        print(request.POST)


class ProfileView(View):
    def get(self, request):
        return render(request, 'Profile/profile.html')

    def post(self, request):
        pass
