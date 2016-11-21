#coding:utf-8
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .user_libs import *
from .course_libs import *
from .common_libs import *

# Create your views here.
def home(request):
    return render(request, "mooc/home.html", {
            "jckc": get_four_courses_of("基础课程"),
            "jptj": get_four_courses_of("精品推荐"),
            "gjjj": get_four_courses_of("高级进阶"),
        })

# Account
def login(request):
    if request.method == "POST":
        if login_check(request.POST.get("email"),
            request.POST.get("password")):
            request.session["user_email"] = request.POST.get("email")
            return json_res(0, '/')
        else:
            return json_res(1, 'Email/Password Error')
    if request.method == "GET":
        if request.session.get('user_id'):
            return redirect('home')
        return render(request, "mooc/login.html")
    raise PermissionDenied


def register(request):
    if request.method == "POST":
        print(request.POST)
        return register_new(request.POST.get("email"),
                request.POST.get("password"),
                request.POST.get("username"))
    raise PermissionDenied


@login_require
def logout(request):
    if request.method == "GET":
        request.session.pop("user_email")
        return redirect('login')
    raise PermissionDenied


# Course list
def courses(request):
    cs = get_all_courses()
    return render(request, "mooc/courses.html", {'courses': cs})


def course(request, _id):
    c = get_one_course(_id)
    ls = get_all_lesson_of(_id)
    return render(request, "mooc/course.html", {'course': c, 'lessons': ls})


# Search
def search(request):
    keyword = request.GET.get("key")
    cs = get_search_course(keyword)
    return render(request, "mooc/search.html", {
        'courses': cs,
        'keyword': keyword
        })


# Exception handle
def PageNotFound(request):
    return render(request, "404.html")


def Forbidden(request):
    return render(request, "403.html")