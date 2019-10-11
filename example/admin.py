from django.contrib import admin
from .models import Simple, UserProfile, User

# Register your models here.
admin.site.register(Simple)
admin.site.register(UserProfile)
admin.site.register(User)
