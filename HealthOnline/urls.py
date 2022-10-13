from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name=''),
    path('about/', views.AboutView.as_view(), name='about'),
    path('appoinment/', views.AppointmentView.as_view(), name='appoinment'),
    path('blog-sidebar/', views.BlogSidebarView.as_view(), name='blog-sidebar'),
    path('blog-single/', views.BlogSingleView.as_view(), name='blog-single'),
    path('confirmation/', views.ConfirmationView.as_view(), name='confirmation'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('department/', views.DepartmentView.as_view(), name='department'),
    path('department-single/', views.DepartmentSingleView.as_view(), name='department-single'),
    path('doctor/', views.DoctorView.as_view(), name='doctor'),
    path('doctor-single/', views.DoctorSingleView.as_view(), name='doctor-single'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('profile/', views.ProfileView.as_view(), name='profile1'),
]
