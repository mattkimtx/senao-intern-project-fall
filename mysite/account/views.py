from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.http import JsonResponse
from .act_pwd_api import user_login, user_signup
import json
import re

@csrf_exempt
def signup(request):
    json_data = user_signup(request)
    return json_data

@csrf_exempt
def login(request):
    json_data = user_login(request)
    return json_data