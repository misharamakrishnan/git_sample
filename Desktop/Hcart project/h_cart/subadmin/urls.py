from django.urls import path
from . import views

app_name = 'subadmin'

urlpatterns = [
    path('login1', views.login1 ,name='login1')
]