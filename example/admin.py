from django.contrib import admin
from .models import Simple, UserProfile, User, Intruder, IPcamera, Errormessage,IPstatus,overviewStatus,daily_feeds,camera_notification

# Register your models here.
admin.site.register(Simple)
admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Intruder)
admin.site.register(IPcamera)
admin.site.register(Errormessage)
admin.site.register(IPstatus)
admin.site.register(overviewStatus)
admin.site.register(daily_feeds)
admin.site.register(camera_notification)
