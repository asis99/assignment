from django.urls import path
# from .views import DashboardView, CourseListView, ProfileView, ContactFormView
from .views import *

# urlpatterns = [
#     path('', DashboardView.as_view(), name='dashboard'),
#     path('courses/', CourseListView.as_view(), name='courses'),
#     path('profile/', ProfileView.as_view(), name='profile'),
#     path('contact/', ContactFormView.as_view(), name='contact'),
# ]

urlpatterns = [
    # path('', DashboardView.as_view(), name='dashboard'),
    path('courses/', GetTotalStats, name='courses'),
]