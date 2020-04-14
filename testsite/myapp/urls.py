from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.hai),
    path('hello/',views.hello),
    path('add',views.add, name='add'),
]