from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
]