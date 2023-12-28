from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .act_pwd_api import user_login, user_signup

@csrf_exempt
def signup(request):
    json_data = user_signup(request)
    return json_data

@csrf_exempt
def login(request):
    json_data = user_login(request)
    return json_data