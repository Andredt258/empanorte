from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('solicitarman/', views.solicitarman , name='solicitarman'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('missolicitudes/', views.missolicitudes , name='missolicitudes'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html") , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="login.html") , name='logout'),
    path('crearusuario/', views.crearusuario , name='crearusuario') ,
]