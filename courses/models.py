from enum import unique
from tabnanny import verbose
from django.db import models

class Base(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  status = models.BooleanField(default=True)

  class Meta:
    abstract = True

class Course(Base):
  title = models.CharField(max_length=255)
  url = models.URLField(unique=True)

  class Meta:
    verbose_name = 'Course'
    verbose_name_plural = 'Courses'

  def __str__(self):
      return self.title

class Assessment(Base):
  course = models.ForeignKey(Course, related_name="Assessments", on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  content = models.TextField(blank=True, default='')
  score = models.DecimalField(max_digits=2, decimal_places=1)

  class Meta:
    verbose_name = "Assessment"
    verbose_name_plural = "Assessments"
    unique_together = ['email', 'course']

  def __str__(self):
      return f'{self.name}: {self.score}'