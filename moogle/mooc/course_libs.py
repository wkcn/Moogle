# -*- utf8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Course, Lesson, Classification
from .common_libs import *
# from .views import login
import re

def get_all_courses():
    return Course.objects.all()

def get_one_course(_id):
    return get_object_or_404(Course, id=_id)

def get_all_lesson_of(_id):
    return get_object_or_404(Course, id=_id).lesson.all()

def get_search_course(keyword):
    return Course.objects.filter(title__icontains = keyword)

def get_four_courses_of(name):
    return get_object_or_404(Classification, name=name).course.all()[:4]

def get_home_numbers():
    return 0,1,2