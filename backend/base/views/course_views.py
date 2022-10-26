from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from base.models import Course
from base.serializers import CourseSerializer
from base.strConst import *


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def getMyCourses(request):
    user = request.user
    
    if request.method == 'GET':
        try:
            courses = user.course_set.all()
        except Course.DoesNotExist:
            return Response({DETAIL: COURSES_NOT_EX_YET}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(CourseSerializer(courses, many=True).data)
    
    elif request.method == 'POST':
        data = request.data
        try:
            Course.objects.create(
                name = data['name'],
                contractNo=data['contractNo'],
                user=user,
            )
            return Response({DETAIL:COURSE_CREATE_SUCCESS}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({DETAIL:COURSE_CREATE_FAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
        