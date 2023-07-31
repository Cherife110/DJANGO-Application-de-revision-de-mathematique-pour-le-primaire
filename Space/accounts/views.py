from django.shortcuts import render

# Create your views here.
def home_teacher(request):
    return render(request, 'accounts/home_teacher.html')
    