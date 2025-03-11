from django.urls import path, reverse_lazy
from . import views
from .views import SignUpView, UserDetailView, UserListView, activate_user
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/',  SignUpView.as_view(), name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'authenticate/login.html', next_page='/users/'), name = 'login' ), 
    path('logout/', auth_views.LogoutView.as_view(template_name = 'authenticate/logout.html', next_page = "login"), name = 'logout'),  
    path('activate/<str:token>/', activate_user, name = 'activate'), 
    path('user_list/', UserListView.as_view(), name = 'user_list'),
    path('user_list/<int:pk>/', UserDetailView.as_view(), name = 'user_detail'),
    path('update/<int:pk>', views.UserUpdateView.as_view(), name = 'user_update'),
]