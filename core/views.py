from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# class DashboardView(TemplateView):
#     template_name = "core/dashboard.html"

# class CourseListView(TemplateView):
#     template_name = "core/courses.html"

# class ProfileView(TemplateView):
#     template_name = "core/profile.html"

# class ContactFormView(TemplateView):
#     template_name = "core/contact.html"


@api_view(['GET'])
def GetTotalStats(request):
    stud_data = StudentsModel.objects.count()
    course_data =  CoursesModel.objects.count()
    if stud_data and course_data:
        return Response(data={'total_students':stud_data,  
                              'total_courses':course_data
                              }, 
                              status=status.HTTP_200_OK)
    return Response(data={'total_students':0,  'total_courses':0
                              }, status=status.HTTP_200_OK)





