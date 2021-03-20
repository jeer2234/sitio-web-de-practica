# urls from homepage
from django.urls import path, include
from . import views

app_name = 'homepage'

urlpatterns = [

    path('', views.index, name= 'index'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),
    path('services', views.services, name= 'services'),

]