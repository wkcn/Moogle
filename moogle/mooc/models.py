# -*- coding=utf8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def is_authenticated():
        return True

    def __str__(self):
        return "User <%s>" % self.username


class Course(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=1024, blank=True)
    teacher = models.CharField(max_length=128, blank=True)
    school = models.CharField(max_length=256, blank=True)
    mtime = models.DateTimeField(auto_now=True)
    ctime = models.DateTimeField(auto_now_add=True)
    mark_num = models.IntegerField(default=0)
    begin_time = models.CharField(max_length=128, blank=True)
    schedule = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return "Course <%s>" % self.title


class Lesson(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.TextField(max_length=512, blank=True)
    mtime = models.DateTimeField(auto_now=True)
    ctime = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=256, blank=True)
    order = models.IntegerField(default=-1)
    
    course = models.ForeignKey('Course', related_name='course')

    def __str__(self):
        return "Lesson <%s>" % self.title