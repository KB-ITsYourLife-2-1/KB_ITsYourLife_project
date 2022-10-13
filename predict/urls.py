


from django.urls import path
from . import views

urlpatterns = [
    path("", views.total, name="predict"),
    path("product_1/", views.p1, name="predict_1"),
    path("product_2/", views.p2, name="predict_2"),
    path("product_3/", views.p3, name="predict_3"),
    path("product_4/", views.p4, name="predict_4"),
    path("product_5/", views.p5, name="predict_5"),
    path("product_6/", views.p6, name="predict_6"),
    path("product_7/", views.p7, name="predict_7"),
    path("product_8/", views.p8, name="predict_8"),
]