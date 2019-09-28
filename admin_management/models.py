from django.db import models
from django.utils import timezone
#from admin_management import LineAPI

# Create your models here.

class Intruder(models.Model) : 
    intru = models.CharField(max_length=20)
    cam = models.CharField(max_length=10)
    timedetect = models.DateTimeField('TD', default=timezone.now())

    #def lineintruder(self):
    #   LineAPI.lineNotify('Detect Intruder')
         
