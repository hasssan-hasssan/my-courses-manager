from django.contrib.auth.hashers import make_password

from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializers import UserSerializer

class MyCreatorTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializer(self.user).data

        for k, v in serializer.items():
            data[k] = v

        return data


class MyCreatorTokenView(TokenObtainPairView):
    serializer_class = MyCreatorTokenSerializer
    
   
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def userProfile(request):
    user = request.user
    if request.method == 'GET':
        return Response(UserSerializer(user,many=False).data)
    
    elif request.method == 'PUT':
        data = request.data
        user.first_name = data['name']
        if data['password'] != "":
            user.password = make_password(data['password'])
        user.save()
        return Response(UserSerializer(user,many=False).data)
    
    