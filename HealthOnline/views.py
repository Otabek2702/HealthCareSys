from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Room, Patient, Visits, Payment, PaymentType, Doctor, Appointment, Department, Specialization


# Create your views here.


class IndexView(View):

    def get(self, request):
        context = {'department': Department.objects.all()}
        print(request.GET)
        return render(request, "onlineView/index.html", context=context)

    def post(self, request):
        print(request.POST)


def login_user(request):
    print(request.method)
    if request.method == "POST":
        print(request.method)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, "Bunday foydalanauvchi topilmadi. Qaytadan urinib ko'ring!")
            return redirect('login')
    else:
        return render(request, 'onlineView/signup_login.html')


class ProfileView(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = 'patient'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'Profile/profile.html')

    def post(self, request):
        pass
