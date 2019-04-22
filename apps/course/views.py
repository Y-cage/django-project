#!/usr/bin/env python
# coding=utf-8

# Author:cage
# views.py 2019-04-16 12:36

from django.shortcuts import render,reverse
from .models import Course

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required



def course_index(request):
    context = {
        'courses': Course.objects.all()

    }
    return render(request, 'course/course_index.html', context=context)

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    context = {
        'course': course
    }
    return render(request, 'course/course_detail.html', context=context)


def course_order(request, course_id):
    course = Course.objects.get(pk=course_id)
    context = {
        'course': course
    }
    return render(request, 'course/course_order.html', context=context)

def pay(request):
    return render(request, 'course/pay.html')

