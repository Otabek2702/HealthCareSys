from django.urls import path
from .views import IndexView, ProfileView, login_user

urlpatterns = [
    path('', IndexView.as_view(), name=''),
    path('login/', login_user, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
