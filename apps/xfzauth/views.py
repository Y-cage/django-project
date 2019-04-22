#!/usr/bin/env python
# coding=utf-8

# Author:cage
# views.py 2019-04-15 15:19


from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_POST
from .forms import LoginForm, RegisterForm
from django.http import JsonResponse
from utils import restful
from django.shortcuts import redirect,render
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()
# 处理前段post请求
@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = authenticate(request, username=telephone, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return render(request, 'news/index.html')

            else:
                return restful.unauth(message='您的账号被冻结')
        else:
            return restful.params_error(message='手机号或者密码错误')
    else:
        errors = form.get_errors()
        return restful.params_error(message=errors)

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))

@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(telephone=telephone, username=username, password=password)

        login(request, user)

        return render(request, 'news/index.html', {'user.username': user.username})
    else:
        return restful.params_error(message=form.get_errors())



