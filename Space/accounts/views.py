from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib.messages import success, error
from django.contrib.auth.decorators import login_required
from .forms import ParentCreationForm, EleveCreationForm, ProfesseurCreationForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        # Récupération du rôle choisi par l'utilisateur
        role = request.POST.get('role')
        # Sélection du formulaire correspondant au rôle choisi
        if role == 'parent':
            form = ParentCreationForm(request.POST)
        elif role == 'eleve':
            form = EleveCreationForm(request.POST)
        elif role == 'professeur':
            form = ProfesseurCreationForm(request.POST)
        else:
            # Affichage d'un message d'erreur si le rôle est invalide
            error(request, "Rôle invalide")
            return redirect('register')
        # Validation du formulaire
        if form.is_valid():
            # Sauvegarde de l'utilisateur dans la base de données
            user = form.save()
            # Ajout du rôle à l'utilisateur
            group = Group.objects.get(name=role)
            user.groups.add(group)
            # Connexion de l'utilisateur
            login(request, user)
            # Affichage d'un message de succès
            success(request, "Inscription réussie")
            # Redirection vers la page d'accueil en fonction du rôle
            if role == 'parent':
                return redirect('parent_home')
            elif role == 'eleve':
                return redirect('eleve_home')
            elif role == 'professeur':
                return redirect('professeur_home')
        else:
            # Affichage du formulaire avec les erreurs
            return render(request, 'accounts/register.html', {'form': form})
    else:
        # Affichage du formulaire vide
        form = None
        return render(request, 'accounts/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        # Récupération du nom d'utilisateur et du mot de passe saisis par l'utilisateur
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authentification de l'utilisateur
        user = authenticate(username=username, password=password)
        if user is not None:
            # Connexion de l'utilisateur
            login(request, user)
            # Redirection vers la page d'accueil en fonction du type d'utilisateur
            if user.user_type == 'ELEVE':
                return redirect('eleve_home')
            elif user.user_type == 'PARENT':
                return redirect('parent_home')
            elif user.user_type == 'PROFESSEUR':
                return redirect('professeur_home')
            else:
                return redirect('/')
        else:
            # Affichage d'un message d'erreur si l'authentification échoue
            return render(request, 'accounts/login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect'})
    else:
        # Affichage du formulaire de connexion vide
        return render(request, 'accounts/login.html')

# Exemple d'une vue protégée par le décorateur login_required
@login_required(login_url='custom_login')
def eleve_home(request):
    # Affichage de la page d'accueil pour les élèves
    return render(request, 'eleve_home.html')
def home_teacher(request):
    return render(request, 'accounts/home_teacher.html')
