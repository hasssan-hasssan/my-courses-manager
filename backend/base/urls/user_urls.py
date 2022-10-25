from django.urls import path
from base.views import user_views as views

urlpatterns = [
    path('login/', views.MyCreatorTokenView.as_view(), name='login'),
]
