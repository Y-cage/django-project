#!/usr/bin/env python
# coding=utf-8

# Author:cage
# urls.py 2019-04-15 13:57

from django.urls import path
from . import views
from . import course_views, staff_views
app_name = 'cms'

urlpatterns = [
        path('', views.index, name='index'),
        path('news_list/', views.NewsListView.as_view(), name='news_list'),
        path('write_news/', views.WriteNewsViews.as_view(), name='write_news'),
        path('edit_news/', views.EditNewsView.as_view(), name='edit_news'),
        path('delete_news/', views.delete_news, name='delete_news'),
        path('news_category/', views.news_category, name='news_category'),
        path('add_news_category/', views.add_news_category, name='add_news_category'),
        path('edit_news_category/', views.edit_news_category, name='edit_news_category'),
        path('delete_news_category/', views.delete_news_category, name='delete_news_category'),
        path('upload_file/', views.upload_file, name='upload_file')
]

urlpatterns += [
        path('pub_course/', course_views.PubCourseView.as_view(), name='pub_course')
]

urlpatterns += [
        path('staffs/', staff_views.staffs_views, name='staffs'),
        path('add_staff/', staff_views.AddStaffView.as_view(), name='add_staff')
]



