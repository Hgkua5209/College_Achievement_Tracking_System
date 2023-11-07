from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    studentId = models.CharField(max_length=12, primary_key = True)
    studentName = models.CharField(max_length = 128)
    studentCourse = models.CharField(max_length= 128)
    studentPhone = models.CharField(max_length = 128)
    studentEmail = models.CharField(max_length= 128)
    studentAddress = models.CharField(max_length= 128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.studentName

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='users')
    # Add any other user-related fields

    def __str__(self):
        return self.user.username

class Advisor(models.Model):
    advisorId = models.CharField(max_length = 12, primary_key = True)
    advisorName = models.CharField(max_length = 128)
    advisorPhone = models.CharField(max_length = 128)
    advisorEmail = models.CharField(max_length = 128)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.advisorName
    
class SportsClubs(models.Model):
    sportClubsCode = models.CharField(max_length=12, primary_key = True)
    sportClubsName = models.CharField(max_length = 128)
    sportClubsDescription = models.TextField(max_length = 128)

    def __str__(self):
        return self.sportClubsName

class Achivement(models.Model):
    studentId = models.ForeignKey(Student, on_delete = models.CASCADE)
    advisorId = models.ForeignKey(Advisor, on_delete = models.CASCADE)
    sportClubsCode = models.ForeignKey(SportsClubs, on_delete = models.CASCADE)
    session = models.TextField(max_length = 128)
    date = models.DateField(blank = True, null = True)
    achivement = models.TextField(max_length = 128)
    merit = models.IntegerField(default=0)


class MeritRequest(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='merit_requests/')
    status = models.BooleanField(default=False)  # Set to True when reviewed

    