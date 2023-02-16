from django.contrib import admin
from django.urls import path, include

from django.urls import include, path
from . import views
app_name='Bank_app'

urlpatterns = [
    path('', views.demo,name='demo'),
    path('logout',views.logout,name='logout'),
 ]