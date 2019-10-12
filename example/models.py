from django.db import models
from django.contrib.auth.models import UserManager

class Simple(models.Model):
    text = models.CharField(max_length=10)

    def __str__(self):
        return self.text



class UserProfile(models.Model):
    name = models.CharField(max_length=50,verbose_name="Name")
    login = models.CharField(max_length=(25),verbose_name="Login")
    password = models.CharField(max_length=100, verbose_name="Password")
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born date" , null=True,default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection" , null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)
    date_created = models.DateField(verbose_name="Date of Birthday", auto_now_add=True)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    

    objects = UserManager()


    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name
    
    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.password

class Intruder(models.Model):
    Intru = models.CharField(max_length=10)
    IPcam = models.CharField(max_length=10)
    Time = models.CharField(max_length=30)
    ImageID = models.CharField(max_length=50)


    def __str__(self):
        return self.Intru

    def __str__(self):
        return self.IPcam
    
    def __str__(self):
        return self.Time

    def __str__(self):
        return self.ImageID