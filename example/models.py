from django.db import models

class Simple(models.Model):
    text = models.CharField(max_length=10)