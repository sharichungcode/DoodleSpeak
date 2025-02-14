from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Mapeia a URL raiz para a view home
    path('dashboard/', views.index, name='dashboard_index'),
    path('add_test_words/', views.add_test_words, name='add_test_words'),
]