from django.urls import path,include
from django.contrib import admin
from .import views

urlpatterns = [

    path('details/<int:id>/', views.DetailCarView.as_view(), name='car_details'),
   
]
