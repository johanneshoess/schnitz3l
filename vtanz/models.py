from django.db import models

# Create your models here.
class Article(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=255)
    article_id = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='vtanz/%Y/%m/')
    image_alt = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.headline