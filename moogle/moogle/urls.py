"""moogle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mooc import views as mooc_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mooc_views.home, name='home'),
    # Accounts router
    url(r'^accounts/login/?$', mooc_views.login, name='login'),
    url(r'^accounts/register/?$', mooc_views.register, name='register'),
    url(r'^accounts/logout/?$', mooc_views.logout, name='logout'),
    # Courses
    url(r'^courses/?$', mooc_views.courses, name='courses'),
    url(r'^course/(\d+)?$', mooc_views.course, name='course'),
    # Search
    url(r'^search/?$', mooc_views.search, name='search'),
]


handler404 = 'mooc.views.PageNotFound'
handler403 = 'mooc.views.Forbidden'