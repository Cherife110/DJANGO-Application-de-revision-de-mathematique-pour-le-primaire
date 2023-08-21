from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Exercise, User, Profile

class ParentRegistrationForm(UserCreationForm):
    contact_info = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'contact_info')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'contacts_info':forms.TextInput(attrs={'class':'form-control'})
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'parent'
        if commit:
            user.save()
            Profile.objects.create(user=user, contact_info=self.cleaned_data['contact_info'])
        return user

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'classe','password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'classe': forms.Select(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),          
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user

class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','classe', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'classe': forms.Select(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'}),
            'contacts_info':forms.TextInput(attrs={'class':'form-control'})
            }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'teacher'
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "level", "resource_type", "file"]
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields =["title", "exercise_file","correction_file"]
