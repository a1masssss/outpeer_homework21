from rest_framework import serializers
from .models import Course, User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        teacher = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
        )
        students = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username", many=True
            )
        model = Course
        fields = '__all__'



# class CourseSerializer(serializers.ModelSerializer):
#     title  = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     teacher = serializers.CharField()
#     students = serializers.CharField()
#     start_date = serializers.DateField()
#     end_date = serializers.DateField()
#     created_at = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Course.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.teacher = validated_data.get('teacher', instance.teacher)
#         instance.students = validated_data.get('students', instance.students)
#         instance.start_date = validated_data.get('start_date', instance.start_date)
#         instance.end_date = validated_data.get('end_date', instance.end_date)
#         instance.save()
#         return instance