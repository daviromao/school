from django.contrib import admin

from .models import Course, Assessment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ('title', 'url', 'created_at', 'updated_at', 'active')


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
  list_display = ('course', 'name', 'email', 'score', 'created_at', 'updated_at')
