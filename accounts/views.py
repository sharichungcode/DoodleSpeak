from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect

def auth_modal(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if the user exists
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                return JsonResponse({"status": "success", "message": "Logged in successfully!"})
            else:
                return JsonResponse({"status": "error", "message": "Incorrect password!"})
        else:
            # If user does not exist, create a new one
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return JsonResponse({"status": "success", "message": "New account created and logged in!"})

    return JsonResponse({"status": "error", "message": "Invalid request."})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Logged out successfully!"})

    return JsonResponse({"status": "error", "message": "Invalid request."})

