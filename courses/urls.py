from django.urls import path

from .views import CourseAPIView, AssessmentAPIView

urlpatterns = [
  path('courses/', CourseAPIView.as_view(), name='courses'),
  path('assessments/', AssessmentAPIView.as_view(), name='assessments')
]
