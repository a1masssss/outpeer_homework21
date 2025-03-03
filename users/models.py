from django.db import models

from django.contrib.auth.models import AbstractUser
COURSE_CHOICES = [
    ('AI Engineer', 'AI Engineer'), 
    ('Data Science', 'Data Science'), 
    ('Data Analytics', 'Data Analytics'), 
    ('Python Engineering', 'Python Engineering'),
    ('Investment Analytics', 'Investment Analytics'),
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
