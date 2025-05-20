from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = "core/dashboard.html"

class CourseListView(TemplateView):
    template_name = "core/courses.html"

class ProfileView(TemplateView):
    template_name = "core/profile.html"

class ContactFormView(TemplateView):
    template_name = "core/contact.html"
