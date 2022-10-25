from django.contrib import admin
from base.models import Course , Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['contractNo', 'create', 'update', 'isComplete',]
    list_filter = ['create', 'isComplete',]
    search_fields = ['name',]
    date_hierarchy = ('create')
    

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'lessonNo', 'create', 'update', 'isRecord','isConfirm',]
    list_filter = ['create', 'isRecord', 'isConfirm',]
    search_fields = ['name',]
    date_hierarchy = ('create')
    
