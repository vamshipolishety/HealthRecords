from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Patient(User):
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=1)
    contact = models.CharField(max_length=10)

    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=10)
    medicalconditions = models.CharField(max_length=500)
    alergiesandreactions = models.CharField(max_length=500)
    ongoingmedications = models.CharField(max_length=500)
    familyhistory = models.CharField(max_length=500)
    emergencycontact = models.CharField(max_length=10)

    def _str_(self):
        return self.first_name + " " + self.last_name

    class Meta:
        # managed = False
        db_table = 'Patient'


class Doctor(User):
    dob = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=1)
    contact = models.CharField(max_length=10)
    available = models.CharField(max_length=1)
    name = models.CharField(max_length=100)
    speciality = models.CharField(max_length=500)
    currentlocation = models.IntegerField()

    def _str_(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = 'Doctor'