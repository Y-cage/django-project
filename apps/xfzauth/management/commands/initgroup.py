#!/usr/bin/env python
# coding=utf-8

# Author:cage
# initgroup.py 2019-04-22 11:53

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, ContentType
from apps.news.models import  News,NewsCategory,Comment
from apps.course.models import Course, CourseCategory, Teacher

class Command(BaseCommand):
    def handle(self, *args, **options):
        #编辑组(管理文章，课程，评论)
        edit_content_types = [
            ContentType.objects.get_for_model(News),
            ContentType.objects.get_for_model(NewsCategory),
            ContentType.objects.get_for_model(Comment),
            ContentType.objects.get_for_model(Course),
            ContentType.objects.get_for_model(CourseCategory),
            ContentType.objects.get_for_model(Teacher),
        ]
        edit_permissions = Permission.objects.filter(
            content_type__in=edit_content_types
        )
        editGroup = Group.objects.create(name='edit')
        editGroup.permissions.set(edit_permissions)
        editGroup.save()
        self.stdout.write(self.style.SUCCESS('编辑分组创建完成'))

        #财务组(课程订单)
        #管理员组(编辑组+财务组)
        admin_permissions = edit_permissions #edit_permissions.union(finance_permissions)
        adminGroup = Group.objects.create(name="admin")
        adminGroup.permissions.set(admin_permissions)
        adminGroup.save()
        #超级管理员
        self.stdout.write(self.style.SUCCESS('管理员分组创建完成'))
