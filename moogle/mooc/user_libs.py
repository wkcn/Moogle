# -*- utf8 -*-
from django.shortcuts import render, redirect
from .models import User
from .common_libs import *
# from .views import login
import re

from functools import wraps
def login_require(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if request.session.get('user_email') is None:
            return redirect('login')
        return f(request, *args, **kwargs)
    return decorated_function

def login_check(email, password):
    u = User.objects.filter(email=email.lower()).first()
    return u and u.password == password


def register_new(email, password, username):
    if User.objects.filter(email=email.lower()).first():
        return json_res(1, "该邮箱已注册")
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return json_res(1, "邮箱不合法")
    User.objects.create(email=email.lower(),
        password=password,
        username=username,
        is_active=True)
    return json_res(0, "/")