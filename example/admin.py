from django.contrib import admin
from .models import Simple, UserProfile, User, Intruder

# Register your models here.
admin.site.register(Simple)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Intruder)
