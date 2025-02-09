from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'message': 'User  created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def user_profile_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_data = {
                'username': request.user.username,
                'email': request.user.email,
            }
            return JsonResponse(user_data, status=200)
        else:
            return JsonResponse({'error': 'User  not authenticated'}, status=401)
    return JsonResponse({'error': 'Invalid method'}, status=405)

def status_view(request):
    return JsonResponse({'status': 'alive'}, status=200)