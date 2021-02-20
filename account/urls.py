from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('', views.form, name = 'form'),
    path('logout', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
 ]
 