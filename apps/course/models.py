#!/usr/bin/env python
# coding=utf-8

# Author:cage
# models.py 2019-04-20 22:56

from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)

class Teacher(models.Model):
    username = models.CharField(max_length=100)
    avatar = models.URLField() #头像
    jobtitle = models.CharField(max_length=100)
    profile = models.TextField()

class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('CourseCategory', on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    video_url = models.URLField(blank=True)
    cover_url = models.URLField(blank=True)
    price = models.FloatField()
    duration = models.IntegerField()
    profile = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
