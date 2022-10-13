from django.urls import path
from . import views


urlpatterns = [
    # path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='login'),
    path('activation/<uid64>/<token>', views.activate_user, name='activate'),
]
