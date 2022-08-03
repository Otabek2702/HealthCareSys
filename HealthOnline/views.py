from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
# from django.contrib.auth.decorators import
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


# Create your views here.


class IndexView(View):

    def get(self, request, *args, **kwargs):
        context = {'department': models.Department.objects.all()}
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


class ProfileView(LoginRequiredMixin, DetailView):
    model = models.Patient
    context_object_name = 'patient'
    login_url = '/auth/login/'
    template_name = 'Profile/profile.html'

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        return render(request, 'Profile/profile.html')

    def post(self, request):
        pass
