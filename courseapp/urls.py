
from django.urls import path
from . import views
app_name='courseapp'
urlpatterns = [
    path('',views.course,name='course'),
 
]
