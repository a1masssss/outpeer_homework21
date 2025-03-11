from django.views.generic import ListView, DetailView, UpdateView
from urllib import request
from django.shortcuts import redirect, render
from .models import User
from users.models import EmailActivation
from .forms import UserRegisterForm, UserUpdateForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView


def home(request):
    return render(request, 'authenticate/home.html', {})

class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    template_name = 'authenticate/register.html'

def activate_user(request, token: str):
    activation = EmailActivation.objects.get(token=token)
    activation.is_active = True
    activation.save()
    return redirect('login')


class UserListView(ListView):
    paginate_by = 100
    model = User
    template_name = 'authenticate/user_list.html' 
    context_object_name = 'users'  # Default is "object_list"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['users'])
        return context
    
class UserDetailView(DetailView):
    model = User
    template_name = 'authenticate/user_detail.html'
    context_object_name = 'user'
    ordering =  ['id']  # Default is "object"



class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'authenticate/user_create.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'authenticate/user_update.html'
    success_url = reverse_lazy('user_list')




    