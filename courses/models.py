from django.db import models
from users.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=850000.00)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_taught', limit_choices_to={'role': 'Mentor'})
    students = models.ManyToManyField(User, related_name='courses_enrolled', blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.title






