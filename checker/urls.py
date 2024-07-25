# checker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('check_password/', views.check_password, name='check_password'),
    path('generate_password/', views.generate_password, name='generate_password'),
]
