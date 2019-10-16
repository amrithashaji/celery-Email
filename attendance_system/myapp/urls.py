from django.contrib import admin
from django.urls import path, include
from .views import *
from .api import views

urlpatterns = [
    path('',index,name='index'),
    path('downloademp/',excelGenerator,name='excelGenerator'),
    path('restcall/', views.EmployeeListView.as_view(), name=None)
]