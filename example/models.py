from django.db import models

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


