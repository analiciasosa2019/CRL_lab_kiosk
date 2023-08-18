from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home/"),
    path("attendance/", views.attendance, name="attendance/"),
    path("projects/", views.projects, name="projects/"),
    path("information/", views.information, name="information/"),
]