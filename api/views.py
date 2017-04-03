from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from api.models import Course
from api.models import University
from api.serializers import CourseSerializer
from api.serializers import UniversitySerializer

@api_view(['GET'])
def course_list(request, name):
    try:
       course =  Course.objects.get(name = name.lower())
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course)
    return Response(serializer.data)

@api_view(['GET'])
def University_list(request , name):
    try:
        university = University.objects.get(name =  name.lower())
    except University.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UniversitySerializer(university)
    return Response(serializer.data)



