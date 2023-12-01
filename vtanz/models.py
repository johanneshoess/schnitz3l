from django.db import models


# Create your models here.
class Article(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=255, verbose_name='Überschrift')
    article_id = models.CharField(max_length=255, verbose_name='Artikel Kürzel')
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='vtanz/%Y/%m/', verbose_name='Bild')
    image_alt = models.CharField(max_length=255, blank=True, verbose_name='Bildbeschreibung')
    archived = models.BooleanField(default=False, verbose_name='Archiv')

    def __str__(self):
        return ('-- ARCHIV -- ' if self.archived else '') + self.headline
