from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
    )
    role = models.CharField(max_length=20, choices=ROLES)
    CLASSE = (
        ('CP1', 'CP1'),
        ('CP2', 'CP2'),
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
    )
    classe = models.CharField(max_length=30,choices=CLASSE,blank=True )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=100, blank=True)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=20)

class Resource(models.Model):
    RESOURCE_TYPES = (
        ('pdf', 'PDF'),
        ('video', 'Video'),
        ('quiz', 'Quiz'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='resources/')

class Exercise(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exercise_file = models.FileField(upload_to='exercises/')
    correction_file = models.FileField(upload_to='corrections/')

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    choices = models.TextField()
    correct_answer = models.CharField(max_length=100)

class QuizAttempt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()