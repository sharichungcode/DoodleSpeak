from django.urls import path
from .views import auth_modal, logout_user

urlpatterns = [
    path("auth-modal/", auth_modal, name="auth_modal"),
    path("logout/", logout_user, name="logout_user"),
]