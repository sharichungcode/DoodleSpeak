from django.urls import path
from .views import auth_modal, logout_user
from . import views

urlpatterns = [
    path("auth-modal/", auth_modal, name="auth_modal"),
    path("logout/", logout_user, name="logout_user"),
    path('account/', views.account, name='account'),
    path('update_account/', views.update_account, name='update_account'),
    path('change_password/', views.change_password, name='change_password'),
]