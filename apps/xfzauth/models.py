#!/usr/bin/env python
# coding=utf-8

# Author:cage
# models.py 2019-04-15 14:28



from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,User
from shortuuidfield import ShortUUIDField
from django.db import models

class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('请输入手机号')
        if not username:
            raise ValueError('请输入用户名')
        if not password:
            raise ValueError('请传入密码')


        user = self.model(
            telephone=telephone,
            username=username,
            **kwargs)
        user.set_password(password)

        user.save()

        return user

    def create_user(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):

    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11, unique=True)
    #email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)   #   是否可用
    is_staff = models.BooleanField(default=False) #   默认是员工
    is_superuser = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)   #   自动记录加入时间

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username