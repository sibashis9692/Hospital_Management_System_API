from django.db import models
from django.contrib.auth.models import AbstractUser
from Home_app.manager import userManager
# Create your models here.


TYPES = (
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
)

class Departments(models.Model):
    Name = models.CharField(max_length=1000)
    Diagnostics = models.CharField(max_length=1000)
    Location = models.CharField(max_length=1000)
    Specialization = models.CharField(max_length=1000)

    object = userManager()


    def __str__(self):
        return self.Name
    
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=False)
    email = models.EmailField(unique=True)
    Role = models.CharField(max_length=100, choices=TYPES, default=TYPES[0])
    Department_name = models.ForeignKey(Departments, on_delete= models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return self.username
    
    
class Patient_Records(models.Model):
    Patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateField(auto_now_add = True)
    Diagnostics = models.CharField(max_length=1000)
    Observations = models.CharField(max_length=1000)
    Treatments = models.CharField(max_length=1000)