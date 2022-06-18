from django.urls import path
from .views import PatientViewSet, DoctortViewSet, PatientCreateView, PatientUpdateView, PatientDeleteView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView,)


urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('patients/', PatientViewSet.as_view({'get': 'list'}), name='patient'),
    path('doctors/', DoctortViewSet.as_view({'get': 'list'}), name='doctor'),
    path('patients/create', PatientCreateView.as_view(), name='createpatient'),
    path('patients/update', PatientUpdateView.as_view(), name='updatepatient'),
    path('patients/delete', PatientDeleteView.as_view(), name='deletepatient'),
]
