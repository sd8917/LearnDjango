
from django.urls import path
from . import views

app_name = 'accountapp'
urlpatterns = [
    
    path('', views.myaccount, name='myaccount'),
    path('register/', views.register, name='register'),

]
