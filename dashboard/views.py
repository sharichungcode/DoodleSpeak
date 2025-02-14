from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dashboard
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html') 

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

@login_required
def add_test_words(request):
    try:
        dashboard = Dashboard.objects.get(user=request.user)
    except Dashboard.DoesNotExist:
        dashboard = Dashboard.objects.create(user=request.user)

    word_count = len(dashboard.words_history) + 1
    dashboard.words_history.extend([f'word{word_count}'])
    dashboard.save()

    return redirect('dashboard_index')