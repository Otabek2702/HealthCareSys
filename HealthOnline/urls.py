from django.urls import path
from .views import IndexView, ProfileView

urlpatterns = [
    path('', IndexView.as_view(), name=''),
    path('profile/', ProfileView.as_view(), name='profile'),
]
