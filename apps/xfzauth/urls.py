#!/usr/bin/env python
# coding=utf-8

# Author:cage
# urls.py 2019-04-15 15:53

from django.urls import path
from . import views

app_name = 'xfzauth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

