from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
  CourseAPIView,
  CoursesAPIView,
  AssessmentAPIView,
  AssessmentsAPIView,
  CourseViewSet,
  AssessmentViewSet,
)

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('assessments', AssessmentViewSet)


urlpatterns = [
  path('courses/', CoursesAPIView.as_view(), name='courses'),
  path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
  path('courses/<int:course_pk>/assessments', AssessmentsAPIView.as_view(), name='course_assessments'),
  path('courses/<int:course_pk>/assessments/<int:assessment_pk>', AssessmentAPIView.as_view(), name= 'course_assessment'),

  path('assessments/', AssessmentsAPIView.as_view(), name='assessments'),
  path('assessments/<int:assessment_pk>', AssessmentAPIView.as_view(), name='assessment')
]
