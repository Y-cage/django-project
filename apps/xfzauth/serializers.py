#!/usr/bin/env python
# coding=utf-8

# Author:cage
# serializers.py 2019-04-19 12:05

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'telephone', 'username', 'is_active', 'is_staff', 'is_active')
