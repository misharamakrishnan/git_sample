from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('reg', views.reg ,name='reg')
]