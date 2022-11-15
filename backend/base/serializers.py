from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Course, Lesson
import datetime


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','name', 
                  'email', 'is_active', 'is_superuser']
    
    def get_name(self, obj):
        return obj.first_name
    
    
class CourseSerializer(serializers.ModelSerializer):
    timeCourse = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = ['name', 'contractNo', 'create', 'update', 'isComplete', 'user', 'timeCourse' ]
        
    def get_timeCourse(self,obj):
        lessons = obj.lesson_set.all()
        minutes, seconds = 0, 0
        for lesson in lessons:
            minutes += lesson.minute
            seconds += lesson.second
        all = (minutes * 60) + seconds
        return str(datetime.timedelta(seconds=all))
        
            
        
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"