from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("poblar/<int:año>", views.getapi, name="poblar"),
]
