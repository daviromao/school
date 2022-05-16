from django.urls import path

from .views import CourseAPIView, CoursesAPIView, AssessmentAPIView, AssessmentsAPIView

urlpatterns = [
  path('courses/', CoursesAPIView.as_view(), name='courses'),
  path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
  path('courses/<int:course_pk>/assessments', AssessmentsAPIView.as_view(), name='course_assessments'),
  path('courses/<int:course_pk>/assessments/<int:assessment_pk>', AssessmentAPIView.as_view(), name= 'course_assessment'),

  path('assessments/', AssessmentsAPIView.as_view(), name='assessments'),
  path('assessments/<int:assessment_pk>', AssessmentAPIView.as_view(), name='assessment')
]
