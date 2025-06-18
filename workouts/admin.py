from django.contrib import admin
from .models import Workout
from .models import Exercise

# Register your models here.

admin.site.register(Workout)
admin.site.register(Exercise)