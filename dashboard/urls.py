from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.index, name='dashboard_index'), 

    # path('game/', views.game, name='game'),
    path('index/', views.index, name='dashboard_index'),    
    # path('add_test_words/', views.add_words, name='add_test_words'),
]