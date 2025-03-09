from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import EmailActivation, User


class UserRegisterForm(UserCreationForm):
   
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        


    def save(self, commit=...):
        user: User = super().save(commit)
        if not user.is_active:
            activation = EmailActivation.objects.create(user=user)
            activation.send_email()
        return user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'course', 'role', 'is_active']
        # widgets = {
        #     'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        # }

