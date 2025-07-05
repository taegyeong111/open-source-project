from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    average_score = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.title

    def update_average_score(self):
        # Ratings 테이블에서 이 프로젝트의 평균 점수 계산
        self.average_score = self.ratings.aggregate(Avg('score'))['score__avg'] or 0.0
        self.save()

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.title} - {self.score}"

# Rating 저장 후, 해당 Project의 평균 점수를 업데이트하는 시그널
@receiver(post_save, sender=Rating)
def update_project_average_score(sender, instance, **kwargs):
    instance.project.update_average_score()