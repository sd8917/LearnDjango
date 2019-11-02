
from django.urls import path
from .import views

app_name ="blog"

urlpatterns = [
    
    path('',views.blog,name='blog'),
    path('blog/<slug:slug>/',views.blogdetail,name='detail'),
]
