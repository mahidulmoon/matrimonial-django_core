from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileModel(admin.ModelAdmin):
    list_display = ('firstname','religion')



admin.site.register(Profile,ProfileModel)