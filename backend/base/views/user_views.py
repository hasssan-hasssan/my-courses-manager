from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializers import UserSerializer
from base.strConst import *
from base.utils.email_utils import activation_email

import jwt


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
    

@api_view(['POST'])
def registerUser(request):
    data = request.data
    username = data['email']
    password = data['password']
    
    try:
        user = User.objects.create(
            username = data['email'],
            email = data['email'],
            password = make_password(data['password']),
            first_name = data['name'],
            is_active=False
        )
        if(activation_email(user)):
            return Response({DETAIL: WELCOME_TO_MCM}, status=status.HTTP_201_CREATED)
        else:
            return Response({DETAIL: ERR_SENT_EMAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        # کاربری با ایمیل مشابه در دیتابیس هست. حالا یا فعال نیست یا گذرواژه خودرا فراموش کرده
        user = User.objects.get(username=username)
        user.password = make_password(password)
        if user and not user.is_active:
            if(activation_email(user)):
                return Response({DETAIL:ACCOUNT_IS_EX_BUT_NOT_ACTIVE}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({DETAIL: ERR_SENT_EMAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        elif user and user.is_active:
            return Response({DETAIL: PLEASE_LOGIN}, status=status.HTTP_400_BAD_REQUEST)
           

@api_view(['GET'])
def verifyEmail(request, token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, ['HS256'])
        user = User.objects.get(id=payload['user_id'])
        user.is_active = True
        user.save()
        return Response({DETAIL: ACTIVATOIN_SUCCESS}, status=status.HTTP_200_OK)
    except:
        return Response({DETAIL: ACTIVATOIN_FAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)