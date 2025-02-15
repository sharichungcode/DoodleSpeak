"""
URL configuration for web_doodlespeak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from dashboard import views as dashboard_views
from profile import views as profile_views


urlpatterns = [
    # path('', dashboard_views.index, name='index'),
    # path('', include('index.urls')),
    path('', include('dashboard.urls')), 
    path('admin/', admin.site.urls),
    path('game/', profile_views.game, name='game'),
    # path('', include('dashboard.urls')), 
    # path('register/', dashboard_views.register, name='register'),
    # path('add_word/', dashboard_views.add_word, name='add_word'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)