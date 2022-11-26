from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(userC_profile)
class Profile_userC(admin.ModelAdmin):
    list_display = [field.name for field in userC_profile._meta.get_fields()]

@admin.register(teams)
class teamsAd(admin.ModelAdmin):
    list_display = [field.name for field in teams._meta.get_fields()]

@admin.register(projects)
class projectsAd(admin.ModelAdmin):
    list_display = [field.name for field in projects._meta.get_fields()]

