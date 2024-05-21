from django.urls import path
from . import views

urlpatterns = [
    path('solicitarman/', views.solicitarman , name='solicitarman'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('missolicitudes/', views.missolicitudes , name='missolicitudes'),
    path('login/', views.login , name='login'),
]