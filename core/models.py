from django.db import models

# Create your models here.
class StudentsModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now=True)


class CoursesModel(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField()
    credits = models.IntegerField()


class EnrollmentModel(models.Model):
    # student	ForeignKey	Related to Student, on_delete=models.CASCADE
    # course	ForeignKey	Related to Course, on_delete=models.CASCADE
    # date_enrolled	DateField	Date when enrollment occurred
    student = models.ForeignKey(to=StudentsModel, on_delete=models.CASCADE, to_field='id')
    course = models.ForeignKey(to=CoursesModel, on_delete=models.CASCADE, to_field='id')
    date_enroll = models.DateField()

class ContactMessage(models.Model):
    # name	CharField	Max length: 100
    # email	EmailField	Email of the sender
    # message	TextField	The message content
    # created_at	DateTimeField	Auto-generated timestamp (auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message= models.TextField()
    created_at = models.DateTimeField()

