from django.db import models


class Quest(models.Model):
    name = models.CharField(max_length=50)
    # Informationen/klappentext
    blurb = models.TextField()
    task = models.TextField()
    image = models.ImageField(upload_to='quest/% Y % m % d/')