from django.db import models

# Create your models here.

class ClientAppointment(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    mobile_number = models.CharField(max_length=50)
    email_address = models.CharField(max_length=150, null=True)
    selected_property = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.DateTimeField()
