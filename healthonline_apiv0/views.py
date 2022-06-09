import json

from django.shortcuts import render
from rest_framework import viewsets, generics
from HealthOnline.models import *
from .serializer import *
from HealthOnline.models import *


# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request):
        def get_queryset(self):
            q = Patient.objects.all()
            url_dict = self.request.GET
            if 'patient_name' in url_dict['patient_name']:
                q = q.filter(first_name__icontains=url_dict.get('patient_name'))
                print(q)
            return q


class DoctortViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientCreateView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)


class PatientUpdateView(generics.UpdateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    # lookup_field = 'id'

    def get_object(self):
        return Patient.objects.get(pk=self.request.data.get('id'))

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class PatientDeleteView(generics.DestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def get_object(self):
        return Patient.objects.get(pk=self.request.data.get('id'))

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
