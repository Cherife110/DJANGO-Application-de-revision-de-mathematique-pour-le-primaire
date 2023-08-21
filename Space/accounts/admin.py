from django.contrib import admin
from .models import Exercise, User , Profile ,Course

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Exercise)