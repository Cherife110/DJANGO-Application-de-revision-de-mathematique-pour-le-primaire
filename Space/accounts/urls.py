from django.urls import path
from .views import home_teacher
urlpatterns = [
    path("home_teacher", home_teacher, name = "home_teacher_page")
]