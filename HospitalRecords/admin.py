from django.contrib import admin
from.models import Patient,Doctor

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'dob', 'contact', 'address','gender')

# Register your models here.
admin.site.register(Patient,PatientAdmin)
admin.site.register(Doctor)
