from django.urls import path
from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/',  SignUpView.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'authenticate/login.html', next_page="/"), name = 'login' ), 
    path('logout/', auth_views.LogoutView.as_view(template_name = 'authenticate/logout.html', next_page = "login"), name = 'logout'),   
]