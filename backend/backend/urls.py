from django.contrib import admin
from django.urls import path, include

urls = [
    path('users/', include('base.urls.user_urls')),
    path('courses/', include('base.urls.course_urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(urls)),
]