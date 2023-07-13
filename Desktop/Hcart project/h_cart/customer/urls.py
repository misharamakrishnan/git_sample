from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('reg1', views.reg1 ,name='reg1')
]