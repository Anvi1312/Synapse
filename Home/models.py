from django.db import models
from django.db import models

from django.db import models

from django.db import models

from django.db import models
from django.utils import timezone




class Appointment(models.Model):
    appointment_date = models.DateTimeField(default=timezone.now)  # Set a default value
    notes = models.TextField(blank=True, null=True)
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled')

    def __str__(self):
        return f"Appointment with {self.doctor_name} on {self.appointment_date.strftime('%Y-%m-%d %H:%M:%S')}"
class PatientRegistrationForm(models.Model):
    TITLE_CHOICES = [
        ('mr', 'Mr.'),
        ('mrs', 'Mrs.'),
        ('ms', 'Ms.'),
        ('dr', 'Dr.'),
    ]

    GENDER_CHOICES = [
        ('male', 'Identifies as Male'),
        ('female', 'Identifies as Female'),
    ]

    SEX_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('unknown', 'Unknown'),
    ]

    SEXUAL_ORIENTATION_CHOICES = [
        ('straight', 'Straight'),
        ('lesbian', 'Lesbian'),
        ('bisexual', 'Bisexual'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
    ]

    title = models.CharField(max_length=4, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    birth_first_name = models.CharField(max_length=50)
    birth_middle_name = models.CharField(max_length=50, blank=True, null=True)
    birth_last_name = models.CharField(max_length=50)

    dob = models.DateField()  # Date of Birth
    gender_identity = models.CharField(max_length=10, choices=GENDER_CHOICES)
    sex = models.CharField(max_length=7, choices=SEX_CHOICES)
    sexual_orientation = models.CharField(max_length=10, choices=SEXUAL_ORIENTATION_CHOICES)
    marital_status = models.CharField(max_length=7, choices=MARITAL_STATUS_CHOICES)

    address = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50, default='India')

    mobile_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)

    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)

    email = models.EmailField()
    aadhaar_number = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f'{self.title} {self.first_name} {self.last_name}'

