from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def auth_modal(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if the user exists
        if User.objects.filter(email=email).exists():
            user = authenticate(request, username=User.objects.get(email=email).username, password=password)
            
            if user:
                login(request, user)
                return JsonResponse({"status": "success", "message": "Logged in successfully!"})
            else:
                return JsonResponse({"status": "error", "message": "Incorrect password!"})
        else:
            # If user does not exist, create a new one
            username = email.split('@')[0]  # Use the part before @ as username
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return JsonResponse({"status": "success", "message": "New account created and logged in!"})

    return JsonResponse({"status": "error", "message": "Invalid request."})

@login_required
def account(request):
    return render(request, 'access/account.html')

@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('name')
        user.email = request.POST.get('email')
        user.save()
        return redirect('account')
    return redirect('account')

@login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            return JsonResponse({"status": "success", "message": "Password changed successfully!"})
        else:
            return JsonResponse({"status": "error", "message": "Passwords do not match!"})

    return JsonResponse({"status": "error", "message": "Invalid request."})

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Logged out successfully!"})
    return JsonResponse({"status": "error", "message": "Invalid request."})

