from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Parent, Eleve, Professeur

class ParentCreationForm(UserCreationForm):
    # Ajout des champs propres au parent
    firstname = forms.CharField(max_length=150)
    lastname = forms.CharField(max_length=70)
    contact = forms.CharField(max_length=70)
    email = forms.EmailField()
    enfants = forms.ModelMultipleChoiceField(
        queryset=Eleve.objects.all(), # Tous les élèves disponibles
        widget=forms.CheckboxSelectMultiple # Affichage sous forme de cases à cocher
    )

    class Meta:
        model = User # Le modèle associé au formulaire
        fields = ['username', 'password1', 'password2', 'firstname', 'lastname', 'contact', 'email', 'enfants'] # Les champs à afficher dans le formulaire

    def save(self, commit=True):
        # Sauvegarde de l'instance du modèle User
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Création de l'instance du modèle Parent
            parent = Parent.objects.create(user=user)
            # Ajout des enfants sélectionnés au parent
            parent.enfants.set(self.cleaned_data['enfants'])
            parent.save()
        return user
