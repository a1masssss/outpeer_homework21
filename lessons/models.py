from django.db import models

class Lesson(models.Model):
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    url = models.URLField()
    absent_students = models.ManyToManyField('users.User', related_name='absent_students', blank=True) 
    duration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lesson {self.number}"