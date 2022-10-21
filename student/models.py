from django.db import models
from django.forms import CharField
from django.urls import reverse

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length= 255)
    s_class = models.CharField(max_length= 255)
    address = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    def __str__(self):
        return f"mr {self.name} in the {self.s_class} of {self.school_name} School"
    
    def get_absolute_url(self):
        return reverse("home")
    
class S_name(models.Model):
       name = models.CharField(max_length= 255) 
       
       