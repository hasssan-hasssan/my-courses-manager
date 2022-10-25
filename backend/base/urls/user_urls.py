from django.urls import path
from base.views import user_views as views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.MyCreatorTokenView.as_view(), name='login'),
    path('refresh/token/', TokenRefreshView.as_view(), name='refresh_token'),  
    path('register/', views.registerUser, name='user-register'),
    
    path('profile/', views.userProfile, name='user-profile')
] 
