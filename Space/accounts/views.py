from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Course, Exercise, User
from .forms import CourseForm, ExerciseForm, LoginForm, ParentRegistrationForm, StudentRegistrationForm, TeacherRegistrationForm
from django.views.generic import DetailView
def index(request):
    return render(request, "accounts/index.html")

def home_teacher(request):
    return render(request, "accounts/home_teacher.html")

def home_student(request):
    return render(request, "accounts/home_student.html")

def home_parent(request):
    return render(request, "accounts/home_parent.html")
def list_courses(request):
    courses = Course.objects.all() # Récupère tous les cours
    context = {"courses": courses} # Crée un dictionnaire avec les cours
    return render(request, "accounts/liste_cours.html", context) # 
def list_exercise(request):
    exercises = Exercise.objects.all()
    context = {'exercises': exercises }
    return render(request,"accounts/liste_exercice.html" ,context )
def upload_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../../home_teacher')
    else:
        form = CourseForm()
    return render(request, "accounts/course.html", {"form": form})

def upload_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../../home_teacher')
    else:
        form = ExerciseForm()
    return render(request, "accounts/exercice.html", {"form": form})

class CourseDetailView(DetailView):
    model = Course # Le modèle à utiliser
    template_name = "accounts/detail_cours.html" # Le nom du template à utiliser
    pk_url_kwarg = "id" # Le nom du paramètre qui contient l'identifiant de l'objet (par défaut c'est "pk")
    # slug_url_kwarg = "slug" # Le nom du paramètre qui contient le slug de l'objet (par défaut c'est "slug")


def CustomLogin(request):
    template = 'accounts/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=id_number, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'student':
                    return HttpResponseRedirect('home_student')
                elif user.role == 'teacher':
                    return HttpResponseRedirect('home_teacher')
                elif user.role == 'parent':
                    return HttpResponseRedirect('home_parent')
            else:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Authentification invalide. ID ou mot de passe incorrecte'
                })
    else:
        form = LoginForm()
    return render(request, template, {'form': form})


def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'parent':
            return redirect('register_parent')
        elif role == 'student':
            return redirect('register_student')
        elif role == 'teacher':
            return redirect('register_teacher')
        else:
            return render(request, 'accounts/register.html', {'error': 'Veuillez choisir un rôle valide.'})
    else:
        return render(request, 'accounts/register.html')

def register_parent(request):
    if request.method == 'POST':
        form = ParentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ParentRegistrationForm()
    return render(request, 'accounts/register_parent.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parent_dashboard')
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register_student.html', {'form': form})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'accounts/register_teacher.html', {'form': form})
