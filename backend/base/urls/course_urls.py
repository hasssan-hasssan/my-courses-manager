from django.urls import path
from base.views import course_views as views

urlpatterns = [
    path('my/', views.getMyCourses, name='users-courses'),
    path('<str:contNo>/', views.getMyCourse, name='user-course'),
    path('<str:contNo>/l-all/', views.getMyCourseLessons, name='user-courser-lessons')
]
