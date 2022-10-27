from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from base.models import Course, Lesson
from base.serializers import CourseSerializer, LessonSerializer
from base.strConst import *
from base.utils.condition_utils import areLessonsRecordAndConfirm


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def getMyCourses(request):
    user = request.user
    
    if request.method == 'GET':
        try:
            courses = user.course_set.all()
        except:
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


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def getMyCourse(request, contNo):
    user = request.user
        
    try:
        course = user.course_set.get(contractNo=contNo)
    except Course.DoesNotExist:
        return Response({DETAIL:COURSE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            return Response(CourseSerializer(course,many=False).data)
        elif request.method == 'PUT':
            data = request.data
            course.name = data['name']
            if data['isComplete'] == 'True':
                # هر دوره برای تکمیل شدن باید حداقل یک درس تایید شده و ضبط شده داشته باشد
                if len(course.lesson_set.all()) == 0:
                    return Response({DETAIL: COURSE_RULES_1}, status=status.HTTP_400_BAD_REQUEST)
                elif (areLessonsRecordAndConfirm(course)): # آیا همه ی درس ها ضبط و تایید شده
                    course.isComplete = data['isComplete']
                    course.save()
                    return Response(CourseSerializer(course, many=False).data)
                else:
                    return Response({DETAIL: COURSE_LESSONS_ALERT_1}, status=status.HTTP_400_BAD_REQUEST)
            else:
                course.isComplete = data['isComplete']
                course.save()
                return Response(CourseSerializer(course, many=False).data)
        elif request.method == 'DELETE':
            try:
                course.delete()
                return Response({DETAIL: COURSE_DEL_SUCCESS}, status=status.HTTP_200_OK)
            except:
                return Response({DETAIL: COURSE_DEL_FAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
 
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getMyCourseLessons(request, contNo):
    user = request.user
    
    try:
        course = user.course_set.get(contractNo=contNo)
    except Course.DoesNotExist:
        return Response({DETAIL: COURSE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    else:
        if request.method == 'GET':
            lessons = course.lesson_set.all().order_by('lessonNo')
            return Response(LessonSerializer(lessons,many=True).data)     
        
        elif request.method == 'POST':
            data = request.data
            try:
                Lesson.objects.create(
                    course = course, 
                    lessonNo = data['lessonNo'],
                    name = data['name'],
                    description = data['description'],
                )  
                return Response({DETAIL: LESSON_CREATE_SUCCESS}, status=status.HTTP_201_CREATED)
            except:
                return Response({DETAIL: LESSON_CREATE_FAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

@api_view(['GET', 'PUT', 'DELETE'])
def getMyCourseLesson(request, contNo, pk):
    user = request.user
    try:
        course = user.course_set.get(contractNo=contNo)
    except Course.DoesNotExist:
        return Response({DETAIL: COURSE_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    else:
        try:
            lesson = course.lesson_set.get(id=pk)
        except Lesson.DoesNotExist:
            return Response({DETAIL: LESSON_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        else:
            
            if request.method == 'GET':
                return Response(LessonSerializer(lesson, many=False).data)
            elif request.method == 'PUT':
                data = request.data
                
                lesson.lessonNo = data['lessonNo']
                lesson.name = data['name']
                lesson.description = data['description']
                lesson.isRecord = data['isRecord']
                if data['isConfirm'] == 'True': # برای تایید شدن باید چک کنیم که آیا درس ضبط شده یا نه؟
                    if data['isRecord'] == 'True' or lesson.isRecord == True: # ممکن است که ضبط و تایید با هم امده باشند یا از قبل ضبط شده باشد
                        lesson.isConfirm = data['isConfirm']
                        lesson.save()
                        return Response(LessonSerializer(lesson,many=False).data)
                    else:
                        return Response({DETAIL: LESSON_ALERT_1}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    lesson.save()
                    return Response(LessonSerializer(lesson, many=False).data)
            elif request.method == 'DELETE':
                try:
                    lesson.delete()
                    return Response({DETAIL: LESSON_DEL_SUCCESS}, status=status.HTTP_200_OK)
                except:
                    return Response({DETAIL: LESSON_DEL_FAIL}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
