from django.urls import  path
from . import views

urlpatterns = [
    path("", views.Cal, name="Calculator"),
    path("", views.compute, name="Compute"),
    ]