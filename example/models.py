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


class IPcamera(models.Model):
    IPcamera_name = models.CharField(max_length=10)
    IPcamera_status = models.CharField(max_length=10)
    IPconnect_status = models.CharField(max_length=10)
    Background_status = models.CharField(max_length=10)
    Time_log = models.CharField(max_length=10)


    def __str__(self):
        return self.IPcamera_name

    def __str__(self):
        return self.IPcamera_status
    
    def __str__(self):
        return self.IPconnect_statu

    def __str__(self):
        return self.Background_status

    def __str__(self):
        return self.Time_log


class Errormessage(models.Model):
    
    errorID = models.CharField(max_length=10)
    errorName = models.CharField(max_length=20)
    errorTime = models.CharField(max_length=20)
    errorDetail = models.CharField(max_length=50)


   

    def __str__(self):
        return self.errorName
    
    def __str__(self):
        return self.errorTime

    def __str__(self):
        return self.errorDetail

    def __str__(self):
        return self.errorID



class IPstatus(models.Model):
    
    IPnum = models.CharField(max_length=20)
    IPconnect = models.CharField(max_length=10)
    IP_ODconnect = models.CharField(max_length=10)

    def __str__(self):
        return self.IP_ODconnect
    
    def __str__(self):
        return self.IPconnect

    def __str__(self):
        return self.IPnum


class overviewStatus(models.Model):
    
    Over_name = models.CharField(max_length=20)
    Over_num = models.CharField(max_length=10)

    def __str__(self):
        return self.Over_num

    def __str__(self):
        return self.Over_name


class daily_feeds(models.Model):
    
    daily_name = models.CharField(max_length=40)
    daly_time = models.CharField(max_length=20)

    def __str__(self):
        return self.daily_name

    def __str__(self):
        return self.daly_time

    

