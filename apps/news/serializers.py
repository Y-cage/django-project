#!/usr/bin/env python
# coding=utf-8

# Author:cage
# serializers.py 2019-04-19 11:57

from rest_framework import serializers
from .models import News, NewsCategory, Comment
from apps.xfzauth.serializers import UserSerializer

class NewscategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'name')

class NewsSerializer(serializers.ModelSerializer):
    category = NewscategorySerializer()
    author = UserSerializer()
    class Meta:
        model = News
        fields = ('id', 'title', 'desc', 'thumbnail', 'pub_time', 'category', 'author')


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'pub_time')


