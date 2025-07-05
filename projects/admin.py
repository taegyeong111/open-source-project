from django.contrib import admin
from .models import Project, Rating


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','average_score','created_at')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display=('project','score','created_at')