from django.urls import path 
from . import views

urlpatterns=[
    path('myhome/',views.fun1,name="home"),
    path('myhome/',views.fun2,name="myapp"),
    ]