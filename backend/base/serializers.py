from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','name', 
                  'email', 'is_active', 'is_superuser']
    
    def get_name(self, obj):
        return obj.first_name