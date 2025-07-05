from django.contrib import admin
from django.db.models import Avg
from .models import Project, Rating

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_score', 'created_at')
    # ordering = ('-avg_score',)  ❌ 모델 필드가 아니라 주석 처리해야 함

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # annotate 후 정렬을 여기서 처리
        return qs.annotate(avg_score=Avg('ratings__score')).order_by('-avg_score')

    def average_score(self, obj):
        return obj.avg_score if hasattr(obj, 'avg_score') else obj.average_score()
    average_score.short_description = 'Average Score'
    average_score.admin_order_field = 'avg_score'  # annotate와 연결

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('project', 'score', 'created_at')