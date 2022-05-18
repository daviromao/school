from rest_framework import serializers
from .models import Course, Assessment

class AssessmentSerializer(serializers.ModelSerializer):

  class Meta:
    extra_kwargs = {
      'email': {'write_only': True}
    }

    model = Assessment
    fields = (
      'id',
      'course',
      'name',
      'email',
      'content',
      'score',
      'created_at',
      'updated_at',
    )

class CourseSerializer(serializers.ModelSerializer):
  assessments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


  class Meta:
    model = Course
    fields = (
      'id',
      'title',
      'url',
      'created_at',
      'updated_at',
      'active',
      'assessments'
    )
