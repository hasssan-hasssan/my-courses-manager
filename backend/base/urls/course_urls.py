from django.urls import path
from base.views import course_views as views

urlpatterns = [
    path('my/', views.getMyCourses, name='users-courses'),
]