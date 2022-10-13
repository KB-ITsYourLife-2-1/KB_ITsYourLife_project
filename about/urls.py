
from django.urls import path
from . import views

urlpatterns = [
    path("product_1/", views.p1, name="about_1"),
    path("product_2/", views.p2, name="about_2"),
    path("product_3/", views.p3, name="about_3"),
    path("product_4/", views.p4, name="about_4"),
    path("product_5/", views.p5, name="about_5"),
    path("product_6/", views.p6, name="about_6"),
    path("product_7/", views.p7, name="about_7"),
    path("product_8/", views.p8, name="about_8"),
]
