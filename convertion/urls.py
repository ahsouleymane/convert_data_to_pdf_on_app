from django.urls import path
from convertion import views

urlpatterns = [
    path('', views.home, name="home"),
]