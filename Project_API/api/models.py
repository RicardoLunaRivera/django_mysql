from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=50)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=128)
    date_joined = models.DateField()
    is_active = models.BooleanField(default=True)