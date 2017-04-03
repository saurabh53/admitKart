__author__ = 'saurabharora'
from rest_framework import serializers

from api.models import Course, University

class universityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = University()
        fields = ('name','type')
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        university = universityDataSerializer(read_only=False)
        model = Course()
        fields = ('name','fees','duration','university')
class UniversitySerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )
    class Meta:
        model = University()
        fields = ('name', 'rank','year_of_establishment','type','course')