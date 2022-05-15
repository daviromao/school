from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Assessment
from .serializers import CourseSerializer, AssessmentSerializer


class CourseAPIView(APIView):
  """
  API of Courses
  """

  def get(self, request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    
    return Response(serializer.data)

  def post(self, request):
    serializer = CourseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


class AssessmentAPIView(APIView):
  """
  API of Assessments
  """

  def get(self, request):
    assessments = Assessment.objects.all()
    serializer = AssessmentSerializer(assessments, many=True)

    return Response(serializer.data)
  
  def post(self, request):
    serializer = AssessmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
