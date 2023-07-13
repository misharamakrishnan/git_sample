from django.urls import path
from . import views

app_name = 'hadmin'

urlpatterns = [
    path('login', views.login ,name='login')
]