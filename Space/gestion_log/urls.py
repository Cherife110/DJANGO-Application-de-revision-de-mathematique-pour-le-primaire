from django.urls import path
from .views import Home_student , Home_teacher, Register, Login

urlpatterns = [
    path("home_student", Home_student, name='home_student'),
    path('home_teacher', Home_teacher, name='home_teacher'),
    path('register', Register, name="register"),
    path('', Login, name='login_page')
]