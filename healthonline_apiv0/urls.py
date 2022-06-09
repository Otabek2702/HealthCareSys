from django.urls import path
from .views import PatientViewSet, DoctortViewSet, PatientCreateView, PatientUpdateView, PatientDeleteView

urlpatterns = [
    path('patients/', PatientViewSet.as_view({'get': 'list'}), name='patient'),
    path('doctors/', DoctortViewSet.as_view({'get': 'list'}), name='doctor'),
    path('patients/create', PatientCreateView.as_view(), name='createpatient'),
    path('patients/update', PatientUpdateView.as_view(), name='updatepatient'),
    path('patients/delete', PatientDeleteView.as_view(), name='deletepatient'),
]
