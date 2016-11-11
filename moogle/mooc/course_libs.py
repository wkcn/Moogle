# -*- utf8 -*-
from django.shortcuts import render, redirect
from .models import User, Course
from .common_libs import *
# from .views import login
import re

def get_all_courses():
    print(Course.objects.all())
    return Course.objects.all()