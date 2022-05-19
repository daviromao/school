from rest_framework import serializers

from django.db.models import Avg

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

  def validate_score(self, value):
    if value in range(1, 6):
      return value
    
    raise serializers.ValidationError('Score must be integer in range 1-5')

class CourseSerializer(serializers.ModelSerializer):
  assessments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  average_assessments = serializers.SerializerMethodField()

  class Meta:
    model = Course
    fields = (
      'id',
      'title',
      'url',
      'created_at',
      'updated_at',
      'active',
      'assessments',
      'average_assessments',
    )
  
  def get_average_assessments(self, obj):
    average = obj.assessments.aggregate(Avg('score')).get('score__avg')

    if average is None:
      return 0
    
    return round(average * 2) / 2