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
    
   
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def userProfile(request):
    
    if request.method == 'GET':
        user = request.user
        return Response(UserSerializer(user,many=False).data)
    
    