

from django.urls import path
from . import viewstest

urlpatterns = [
    path("register", viewstest.register, name="register" ),
]
