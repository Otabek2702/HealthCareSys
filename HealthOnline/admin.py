from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(PaymentType)
admin.site.register(Visits)
admin.site.register(Appointment)
admin.site.register(Room)
admin.site.register(Patient)
