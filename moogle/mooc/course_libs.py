# -*- utf8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Course, Lesson
from .common_libs import *
# from .views import login
import re

def get_all_courses():
    return Course.objects.all()

def get_one_course(_id):
    return get_object_or_404(Course, id=_id)

def get_all_lesson_of(_id):
    return get_object_or_404(Course, id=_id).course.all()