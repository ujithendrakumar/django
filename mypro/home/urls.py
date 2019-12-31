from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('test/<name>', views.test,name="test"),
]
