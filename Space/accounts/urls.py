from django.urls import path
from .views import home_teacher, register, custom_login
urlpatterns = [
    path("home_teacher", home_teacher, name = "professeur_home"),
    path("register",register, name="register_page"),
    path("login", custom_login, name="custom_login")
]