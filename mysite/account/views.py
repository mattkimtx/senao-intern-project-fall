from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from mongo import user_exists, create_account, verify
from datetime import datetime
import json
import re

def signup(request):
    # password complexity requirement (uppercase, lowercase, number, special character)
    def valid_password(password):
        return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)', password))
    try:
        # HTTP Method
        if request.method == 'POST':    
            data = json.loads(request.body.decode('utf-8'))
            username = data['username']
            password = data['password']

            # check if username and password are valid
            if len(username) < 4 or len(username) > 32:
                return JsonResponse({'success': 'false', 
                                     'error': 'Username length must be between 3-32 characters'}, status=400) # 400 is fail length requirement
            if len(password) < 8 or len(password) > 32:
                return JsonResponse({'success': 'false',
                                     'error': 'Password length must be between 8-32 characters'}, status=400)
            if valid_password(password) == False:
                return JsonResponse({'success': 'false', 
                                     'error': 'Password must contain at least one uppercase, lowercase, and number'}, status=400) # syntax not correct
            
            # check if username already exists
            if user_exists(username):
                    return JsonResponse({'success': 'false', 
                                         'error': 'Username already exists'}, status=400)
            else:
                created_bool = create_account(username, password)
                if created_bool == True:
                    return JsonResponse({'success': 'true',
                                         'error': 'none'}, status=200)
                else:
                    return JsonResponse({'success': 'false', 
                                         'error': 'An error occured while creating the account'}, status=500)
            
        else:
            return JsonResponse({'success': 'false', 
                                 'error': 'invalid HTTP method'}, status=405) 

    except Exception as e:
        return JsonResponse({'success': 'false', 
                             'error': 'an error occured'}, status=500)

def login(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body.decode('utf-8'))
            username = data['username']
            password = data['password']

            # gets timestamp from the request
            timestamp = datetime.now()

            # check if username and password are valid
            valid_account_bool = verify(username, password, timestamp)
            if valid_account_bool == 0:
                return JsonResponse({'success': 'true',
                                     'error': 'none'}, status=200)
            if valid_account_bool == 1:
                                return JsonResponse({'success': 'false', 
                                     'error': 'Invalid username or password'}, status=400)
            else:
                return JsonResponse({'success': 'false', 
                                     'error': 'Invalid username or password'}, status=400)

        else:
            return JsonResponse({'success': 'false', 
                                 'error': 'invalid HTTP method'}, status=405)
    
    except Exception as e:
        return JsonResponse({'success': 'false', 
                             'error': 'an error occured'}, status=500) 