from django.shortcuts import render

# Create your views here.
def Home_student(request):
    return render(request, 'gestion_log/home_student.html')
def Home_teacher(request):
    return render(request, 'gestion_log/home_teacher.html')
def Register(request):
    return render(request, 'gestion_log/register.html')
def Login(request):
    return render(request, 'gestion_log/login.html')