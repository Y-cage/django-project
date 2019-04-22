#!/usr/bin/env python
# coding=utf-8

# Author:cage
# forms.py 2019-04-14 23:58

from django import forms

from apps.forms import FormMixin

class PublicCommentForm(forms.Form, FormMixin):
    content = forms.CharField()
    news_id = forms.IntegerField()


