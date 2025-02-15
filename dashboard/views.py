from django.shortcuts import render, redirect
from .models import Dashboard
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html') 

# def index(request):
#     dashboard = Dashboard.objects.get(user=request.user)
#     return render(request, 'dashboard/index.html', {'dashboard': dashboard})

@login_required
def index(request):
    try:
        dashboard = Dashboard.objects.get(user=request.user)
    except Dashboard.DoesNotExist:
        dashboard = Dashboard.objects.create(user=request.user)
    return render(request, 'dashboard/index.html', {'dashboard': dashboard})