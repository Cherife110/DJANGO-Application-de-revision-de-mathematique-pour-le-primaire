from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_parent, home_student, home_teacher, CustomLogin, index, list_courses, list_exercise, register, register_parent, register_student, register_teacher, upload_course, upload_exercise
urlpatterns = [
    path("home_teacher/upload_course/", upload_course, name="upload_course"),
    path("home_teacher/upload_exercise/", upload_exercise, name="upload_exercise"),
    path("home_teacher/liste_cours", list_courses, name="liste_cours"),
    path("home_teacher/liste_exercise", list_exercise, name="liste_exercise"),
    path("home_teacher", home_teacher, name = "teacher_dashboard"),
    path("home_parent", home_parent, name="parent_dashboard"),
    path("home_student", home_student, name="student_dashboard"),
    path("register/register_parent", register_parent, name="register_parent"),
    path("register/register_student", register_student, name="register_student"),
    path("register/register_teacher", register_teacher, name="register_teacher"),
    path("register",register, name="register_page"),
    path("login", CustomLogin , name="login"),
    path("", index ,name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)