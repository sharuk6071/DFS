from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('api/',views.polls_list, name='polls_list'),
    path('api/<int:pk>/',views.polls_details, name='polls_details'),
    path('',views.index,name='index'),


]
