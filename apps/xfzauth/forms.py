#!/usr/bin/env python
# coding=utf-8

# Author:cage
# forms.py 2019-04-15 15:23


from django import forms
from apps.forms import FormMixin
from django.core.cache import cache
from .models import User

class LoginForm(forms.Form, FormMixin):

    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=10, min_length=6, error_messages=({'max_length':
                                                                                '密码最多不能超过20个字符',

                                                                            'min_length':
                                                                                '密码最少不能少于6个字符'}))
    remember = forms.IntegerField(required=False)

class RegisterForm(forms.Form, FormMixin):
    username = forms.CharField(max_length=20)
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=10, min_length=6, required=False, error_messages=({'max_length':
                                                                                 '密码最多不能超过20个字符',

                                                                             'min_length':
                                                                                 '密码最少不能少于6个字符'}))
    password2 = forms.CharField(max_length=10, min_length=6,required=False, error_messages=({'max_length':
                                                                                 '密码最多不能超过20个字符',

                                                                             'min_length':
                                                                                 '密码最少不能少于6个字符'}))
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        telephone = cleaned_data.get('telephone')

        if password != password2:
            raise forms.ValidationError('两次密码不一致')

        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            forms.ValidationError('该手机号已经被注册')

        exists = User.objects.filter(username=username).exists()
        if exists:
            forms.ValidationError('该用户已经被注册')


