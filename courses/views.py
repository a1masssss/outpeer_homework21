
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status   
from rest_framework.views import APIView


class CourseView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    
    
    def update(self, request):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


