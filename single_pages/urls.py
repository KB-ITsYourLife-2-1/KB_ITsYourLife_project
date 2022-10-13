
from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="home"),
    path("find/", views.find, name="find" )
]
