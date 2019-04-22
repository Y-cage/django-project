#!/usr/bin/env python
# coding=utf-8

# Author:cage
# urls.py 2019-04-14 20:21

from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('<int:news_id>/', views.news_detail, name='news_detail'),
    path('list/', views.news_list, name='news_list'),
    path('public_comment/', views.public_comment, name='public_comment')
]


