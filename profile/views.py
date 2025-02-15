from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import UserForm, ProfileForm
from .models import Profile
from datetime import datetime

# Create your views here.


# def index(request):
#     # return HttpResponse("Hello, world. You're at the profiles index.")
#     return render(request, 'index.html')


def index(request):
    current_year = datetime.now().year
    return render(
        request, 'index.html', {'current_year': current_year}
    )


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'profile/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def add_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        if word and request.user.is_authenticated:
            user_profile = Profile.objects.get(user=request.user)
            user_profile.words_history.append(word)
            user_profile.save()
            return HttpResponse("Word added to history.")
        return render(request, 'profile/add_word.html')
        # return HttpResponse("Failed to add word.")


def game(request):
    return render(request, 'game.html')