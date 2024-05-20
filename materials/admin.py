from django.contrib import admin
from materials.models import Course, Subject


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course',)
    search_fields = ('name', 'course')
