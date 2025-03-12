from rest_framework import serializers
from .models import Lesson
from datetime import timedelta


class LessonSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(write_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'

    def create(self, validated_data):
        validated_data['duration'] = timedelta(hours=validated_data['duration'])
        return super().create(validated_data)
    

    def update(self, instance, validated_data):
        if "duration" in validated_data:
            instance.duration = timedelta(hours=validated_data['duration'])
        return super().update(instance, validated_data)

    