


from django.urls import path
from . import views

urlpatterns = [
    path("", views.total, name="statistic"),
    path("product_1/", views.p1, name="statistic_1"),
    path("product_2/", views.p2, name="statistic_2"),
    path("product_3/", views.p3, name="statistic_3"),
    path("product_4/", views.p4, name="statistic_4"),
    path("product_5/", views.p5, name="statistic_5"),
    path("product_6/", views.p6, name="statistic_6"),
    path("product_7/", views.p7, name="statistic_7"),
    path("product_8/", views.p8, name="statistic_8"),
]
