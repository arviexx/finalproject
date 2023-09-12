from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    DOCTOR_CHOICES = [
        ('Dr. Coleen V. Lee, DMD', 'Dr. Coleen V. Lee, DMD'),
        ('Dr. Arleen Lim-Lee, DMD', 'Dr. Arleen Lim-Lee, DMD'),
    ]

    full_name = models.CharField(max_length=255, default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15, default='')
    email = models.EmailField()
    address = models.CharField(max_length=255, default='')
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField(default=timezone.now)
    doctor = models.CharField(max_length=50, choices=DOCTOR_CHOICES)
    Teeth_Extractions = models.BooleanField(default=False)
    Dental_Cleaning = models.BooleanField(default=False)
    Teeth_Whitening = models.BooleanField(default=False)
    Dental_Crowns = models.BooleanField(default=False)
    Cosmetics_Dentistry = models.BooleanField(default=False)
    approval = models.BooleanField(default=False)
    approval_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date} {self.appointment_time}"
