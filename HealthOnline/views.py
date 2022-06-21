from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView
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


class AboutView(View):
    def get(self, request):
        return render(request, 'onlineView/about.html')


class AppointmentView(View):
    def get(self, request):
        return render(request, 'onlineView/appoinment.html')


class BlogSidebarView(View):
    def get(self, request):
        return render(request, 'onlineView/blog-sidebar.html')


class BlogSingleView(View):
    def get(self, request):
        return render(request, 'onlineView/blog-single.html')


class ConfirmationView(View):
    def get(self, request):
        return render(request, 'onlineView/confirmation.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'onlineView/contact.html')


class DepartmentView(View):
    def get(self, request):
        return render(request, 'onlineView/department.html')


class DepartmentSingleView(View):
    def get(self, request):
        return render(request, 'onlineView/department-single.html')


class DoctorView(View):
    def get(self, request):
        return render(request, 'onlineView/doctor.html')


class DoctorSingleView(View):
    def get(self, request):
        return render(request, 'onlineView/doctor-single.html')


class ServiceView(View):
    def get(self, request):
        return render(request, 'onlineView/service.html')


def login_user(request):
    print(request.method)
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.success(request, "Bunday foydalanauvchi topilmadi. Qaytadan urinib ko'ring!")
                return redirect('login')
        elif 'newusername' in request.POST:
            pass 
    else:
        return render(request, 'onlineView/signup_login.html')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'onlineView/register.html'
    success_url = reverse_lazy('login')


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
