from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Record(models.Model):
    class direction(models.TextChoices):
        IN = 'IN', _('went inside')
        OUT = 'OUT', _('came outside')

    creation_date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField()
    amount_in_ml = models.IntegerField()
    direction = models.CharField(
        max_length=3,
        choices=direction.choices,
        default=direction.IN)
    note = models.TextField(blank=True)
    image = models.ImageField(blank=True)
