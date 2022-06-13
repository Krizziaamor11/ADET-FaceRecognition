from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home,name="home"),
    path('login/', views.loginPage,name="loginpage"),
    path('logout/', views.userout,name="logout"),
    path('register/', views.registerPage,name="registerpage"),
    path('records/', views.records,name="records"),
    path('mystudent/', views.mystudent,name="mystudents"),
    path('manage/', views.managerec,name="manage"),
    path('student/add/', views.addstudent,name="addstudent"),
    
]