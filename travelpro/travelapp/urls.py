from django.contrib import admin
from django.urls import path, include
from . import views
appname='travelapp'
urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),

]