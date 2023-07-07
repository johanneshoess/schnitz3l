from django.db import models
from .chain import Chain


class Team(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE, null=True)
    takes = models.TextField(null=True)
