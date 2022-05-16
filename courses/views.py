from rest_framework.generics import get_object_or_404
from rest_framework import generics

from .models import Course, Assessment
from .serializers import AssessmentSerializer, AssessmentSerializer, CourseSerializer

class CoursesAPIView(generics.ListCreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class AssessmentsAPIView(generics.ListCreateAPIView):
  queryset = Assessment.objects.all()
  serializer_class = AssessmentSerializer

  def get_queryset(self):
      if self.kwargs.get('course_pk'):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

      return self.queryset.all()

class AssessmentAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Assessment.objects.all()
  serializer_class = AssessmentSerializer

  def get_object(self):
    if self.kwargs.get('course_pk'):
      return get_object_or_404(self.get_queryset(),
                               course_id=self.kwargs.get('course_pk'),
                               pk=self.kwargs.get('assessment_pk'))
                               
    return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('assessment_pk'))
