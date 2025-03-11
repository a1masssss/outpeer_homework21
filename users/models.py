from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from functools import partial
COURSE_CHOICES = [
    ('AI Engineer', 'AI Engineer'), 
    ('Data Science', 'Data Science'), 
    ('Data Analytics', 'Data Analytics'), 
    ('Python Engineering', 'Python Engineering'),
    ('Investment Analytics', 'Investment Analytics'),
    ('Stuff', 'Stuff'),
]
ROlE_CHOICES = [
    ('Student', 'Student'), 
    ('Mentor', 'Mentor'), 
    ('TA', 'Teaching Assistant'), 
    ('Manager', 'Manager'), 
    ('Administrator', 'Administrator'), 
]
class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    role = models.CharField(max_length=50, choices=ROlE_CHOICES, default='Student')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return f"{self.email}"
    




get_random_token = partial(get_random_string, 100)
class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token  = models.CharField(max_length=100, unique=True, default=get_random_token)
    is_active = models.BooleanField(default=True)


    def send_email(self):
        subject = 'Activate your account'
        message = f'Click here to activate your account: http://localhost:8000/activate/{self.token}'
        form_email = 'example@mail.com'
        recipient_list = [self.user.email]



        send_mail(subject, message, form_email, recipient_list, fail_silently=False)

        print('*' * 20)
        print('Email sent')
        print('*' * 20)
