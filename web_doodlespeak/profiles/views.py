from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the profiles index.")
    return render(request, 'profiles/index.html')


def index(request):
    current_year = datetime.now().year
    return render(request, 'profiles/index.html', {'current_year': current_year})