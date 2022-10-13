from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from HealthOnline.models import *
from .serializer import *
from HealthOnline.models import *


# Create your views here.


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     print('asda')
    #
    #     def get_queryset(self):
    #         q = Patient.objects.all()
    #         url_dict = self.request.GET
    #         print(url_dict)
    #         if 'patient_name' in url_dict['patient_name']:
    #             q = q.filter(first_name__icontains=url_dict.get('patient_name'))
    #             print(q)
    #         return q


class DoctortViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = (IsAuthenticated,)


class PatientCreateView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return super().post(request, *args, **kwargs)


class PatientUpdateView(generics.UpdateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = (IsAuthenticated,)

    # lookup_field = 'id'

    def get_object(self):
        return Patient.objects.get(pk=self.request.data.get('id'))

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class PatientDeleteView(generics.DestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return Patient.objects.get(pk=self.request.data.get('id'))

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
