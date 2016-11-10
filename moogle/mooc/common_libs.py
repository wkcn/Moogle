#coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render, redirect

def json_res(err, ret):
    return JsonResponse({'code': err, 'ret': ret})