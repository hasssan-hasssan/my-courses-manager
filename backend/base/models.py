from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from .strConst import ZERO_TO_SIXTH_ERROR

class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    contractNo = models.CharField(max_length=100, unique=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    isComplete = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.contractNo
    

class Lesson(models.Model):
    lessonNo = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    isRecord = models.BooleanField(default=False)
    isConfirm =models.BooleanField(default=False) 
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    minute = models.PositiveIntegerField(default= 0, validators=[MinValueValidator(0, message=ZERO_TO_SIXTH_ERROR),MaxValueValidator(60, message=ZERO_TO_SIXTH_ERROR)])
    second = models.PositiveIntegerField(default= 0, validators=[MinValueValidator(0, message=ZERO_TO_SIXTH_ERROR),MaxValueValidator(60, message=ZERO_TO_SIXTH_ERROR)])
    
    def __str__(self):
        return f"{str(self.course.contractNo)} / L- {self.lessonNo}"
    