from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from .models import User

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                if User.objects.filter(email=email).exists():
                    form.add_error('email', 'Email already exists')
                else:
                    user = User.objects.create(email=email)
                    user.set_password(password)
                    user.save()
                    login(request, user)
                    return redirect('home')
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})
