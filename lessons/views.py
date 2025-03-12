from .models import Lesson
from .serializers import LessonSerializer
from rest_framework.response import Response
from rest_framework import status   
from rest_framework.views import APIView

class LessonView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                lesson = Lesson.objects.get(pk=pk)
                serializer = LessonSerializer(lesson)
                return Response(serializer.data, status = status.HTTP_200_OK)
            
            except Lesson.DoesNotExist:
                return Response({"message": "Lesson not found"}, status = status.HTTP_404_NOT_FOUND)
            
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, ):
        lesson = LessonSerializer(data=request.data)
        if lesson.is_valid(raise_exception=True):
            lesson.save()
            return Response(lesson.data, status = status.HTTP_201_CREATED)
        return Response(lesson.errors, status = status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)        
    
    def delete(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            lesson.delete()
            return Response({"message": "Lesson deleted Successfully"}, status = status.HTTP_204_NO_CONTENT)
        except Lesson.DoesNotExist:
            return Response({"message": "Lesson not found"}, status = status.HTTP_404_NOT_FOUND)  



    

