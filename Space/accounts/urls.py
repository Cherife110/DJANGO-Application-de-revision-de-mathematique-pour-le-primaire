from django import views
from django.urls import path
from .views import home_parent, home_student, home_teacher, CustomLogin, index, register, register_parent, register_student, register_teacher
urlpatterns = [
    path("home_teacher", home_teacher, name = "teacher_dashboard"),
    path("home_parent", home_parent, name="parent_dashboard"),
    path("home_student", home_student, name="student_dashboard"),
    path("register/register_parent", register_parent, name="register_parent"),
    path("register/register_student", register_student, name="register_student"),
    path("register/register_teacher", register_teacher, name="register_teacher"),
    path("register",register, name="register_page"),
    path("login", CustomLogin , name="login"),
    path("", index ,name="home"),
]