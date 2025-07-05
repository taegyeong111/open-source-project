from django.contrib import admin
from .models import Project, Rating
from django.db.models.signals import post_save
from django.dispatch import receiver

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_score', 'created_at')
    ordering = ['-average_score']  # 평균 점수 내림차순으로 정렬

    def save_model(self, request, obj, form, change):
        obj.update_average_score()  # 평균 점수 갱신
        super().save_model(request, obj, form, change)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('project', 'score', 'created_at')

# Rating 저장 후, 해당 Project의 평균 점수를 업데이트하는 시그널
@receiver(post_save, sender=Rating)
def update_project_average_score(sender, instance, **kwargs):
    instance.project.update_average_score()