from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, firstname=None, lastname=None, contact=None):
        if not username:
            raise ValueError("Vous devez entrez un nom d'utilisateur")
        user = self.model(username=username)
        user.set_password(password)
        user.firstname = firstname
        user.lastname =lastname
        user.contact = contact
        
        user.save() 
        return user
        
    def create_superuser(self, username, password, firstname=None, lastname=None, contact=None):
        user = self.create_user(username=username, password=password, firstname=firstname, lastname=lastname, contact=contact)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user
class CustomUser(AbstractBaseUser):
    # Ajout d'un champ pour le type d'utilisateur
    username = models.CharField(max_length=70, unique=True, blank=False)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=70)
    contact = models.CharField(max_length=70, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["firstname", "lastname"]
    objects = CustomUserManager()

    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True

    USER_TYPE_CHOICES = (
        ("ELEVE", 'eleve'),
        ("PARENT", 'parent'),
        ("PROFESSEUR", 'professeur'),
    )

# Création de modèles spécifiques pour chaque type d'utilisateur
class Eleve(models.Model):
    # Relation un-à-un avec le modèle User
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Autres champs propres aux élèves
    classe = models.CharField(max_length=50, blank=False)
    etablissement = models.CharField(max_length=200, blank=False)

class Parent(models.Model):
    # Relation un-à-un avec le modèle User
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Autres champs propres aux parents
    enfants = models.ManyToManyField(Eleve)
    email = models.EmailField(unique=True)


class Professeur(models.Model):
    # Relation un-à-un avec le modèle User
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Autres champs propres aux professeurs
    etablissement = models.CharField(max_length=200,blank=False)
    classe = models.CharField(max_length=50,blank=False)
    email = models.EmailField(unique=True)

