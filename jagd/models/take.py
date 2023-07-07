from django.db import models
from .quest import Quest
from .team import Team


class Take(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    answer = models.TextField(null=True)
    image = models.ImageField(upload_to='take/% Y % m % d/')