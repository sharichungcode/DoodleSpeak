from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



# Create your views here.
def game(request):
    return render(request, 'game/game.html')

def game_index(request):
    return render(request, 'index.html')

@login_required
def add_word(request):
    from dashboard.models import Dashboard 
    if request.method == 'POST':
        word = request.POST.get('word') 
        if word:
            dashboard, created = Dashboard.objects.get_or_create(user=request.user)
            word_count = len(dashboard.words_history)
            word_with_count = f"{word}_{word_count + 1}"
            dashboard.words_history.append(word_with_count)
            dashboard.save()
            return redirect('dashboard_index')
    return render(request, 'game/game.html')

def index(request):
    return render(request, 'game/index.html')

