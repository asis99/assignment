from .models import *
from rest_framework.serializers import ModelSerializer


class StudentsSerializer(ModelSerializer):
    class Meta:
        model = StudentsModel
        fields = ['id', 'name', 'email', 'enrollment_date']


class CourseSerializer(ModelSerializer):
    class Meta:
        model = CoursesModel
        fields = ['id', 'title', 'description', 'credits']

    
class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = EnrollmentModel
        fields = ['id', 'student', 'course', 'date_enroll']


class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']