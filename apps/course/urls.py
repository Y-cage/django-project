#!/usr/bin/env python
# coding=utf-8

# Author:cage
# urls.py 2019-04-16 12:36


from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.course_index, name='course_index'),
    path('pay/', views.pay, name='pay'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('course_order/<int:course_id>/', views.course_order, name='course_order'),

]
