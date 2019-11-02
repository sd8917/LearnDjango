
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

#put your app differntiate from the other app
app_name = 'myapp'

urlpatterns = [
    path('',views.index,name='index'),
    
] 
