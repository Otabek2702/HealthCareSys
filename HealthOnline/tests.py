from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from . import models


# Create your tests here.

class DepartmentTestCase(TestCase):

    def setUp(self):
        models.Department.objects.create(title="Allergy and immunology")
        models.Department.objects.create(title="Anesthesiology")
        models.Department.objects.create(title="Dermatology")

        models.Patient.objects.create(first_name='Otabek',
                                      last_name='Nigmonov',
                                      birth_date='2002-04-27',
                                      gender='M',
                                      address='Chilonzor',
                                      phone_number='998933842704',
                                      image=SimpleUploadedFile("test_image.jpg",
                                                               content=open('/home/otabek/Pictures/alba.jpeg',
                                                                            'rb').read(),
                                                               content_type="image/jpeg", ),
                                      is_email_verified=True)
        models.Specialization.objects.create(name='Spec1')
        models.Room.objects.create(number=110, floor=2)
        models.Doctor.objects.create(first_name='Otabek',
                                     last_name='Nigmonov',
                                     birth_date='2002-04-27',
                                     gender='M',
                                     specialization_id=1,
                                     room_id=1,
                                     phone_number='998933842704',
                                     image=SimpleUploadedFile("test_image.jpg",
                                                              content=open('/home/otabek/Pictures/alba.jpeg',
                                                                           'rb').read(),
                                                              content_type="image/jpeg", ),
                                     is_email_verified=True)
        models.PaymentType.objects.create(title='Cash')
        models.Appointment.objects.create(patient_id=1,
                                          department_id=1,
                                          doctor_id=1,
                                          time='2002-05-15',
                                          is_visit=True)
        models.Visits.objects.create(date='2022-05-16',
                                     appointment_id=1)
        models.Payment.objects.create(visit_id=1,
                                      amount=25.22555,
                                      payment_type_id=1,
                                      description='asdad',
                                      is_paid=True)

    def test_creating_model(self):
        """Animals that can speak are correctly identified"""
        allergy = models.Department.objects.get(title="Allergy and immunology")

        self.assertEqual(models.Department.objects.count(), 3)
        self.assertEqual(allergy.title, 'Allergy and immunology')

        self.assertEqual(models.Patient.objects.count(), 1)
        self.assertEqual(models.Specialization.objects.count(), 1)
        self.assertEqual(models.Room.objects.count(), 1)
        self.assertEqual(models.Doctor.objects.count(), 1)
        self.assertEqual(models.PaymentType.objects.count(), 1)
        self.assertEqual(models.Appointment.objects.count(), 1)
        self.assertEqual(models.Visits.objects.count(), 1)
        self.assertEqual(models.Payment.objects.count(), 1)

    def test_delete_model(self):
        models.Doctor.objects.all().delete()
        models.Patient.objects.all().delete()
        models.Specialization.objects.all().delete()
        models.Room.objects.all().delete()
        models.PaymentType.objects.all().delete()
        models.Payment.objects.all().delete()
        models.Visits.objects.all().delete()
        models.Appointment.objects.all().delete()

        self.assertEqual(models.Patient.objects.count(), 0)
        self.assertEqual(models.Doctor.objects.count(), 0)
        self.assertEqual(models.Specialization.objects.count(), 0)
        self.assertEqual(models.Room.objects.count(), 0)
        self.assertEqual(models.PaymentType.objects.count(), 0)
        self.assertEqual(models.Appointment.objects.count(), 0)
        self.assertEqual(models.Visits.objects.count(), 0)
        self.assertEqual(models.Payment.objects.count(), 0)
