from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_index, name='game_index'),
    path('game', views.game, name='game'),
    path('add_word/', views.add_word, name='add_word'),
    path('analyze_image/', views.analyze_image, name='analyze_image'),
]
