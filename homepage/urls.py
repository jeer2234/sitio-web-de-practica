# urls from homepage
from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.visualizar, name= 'visualizar')
]