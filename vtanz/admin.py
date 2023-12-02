from django.contrib import admin
from django.db import models
from .models import Article
from pagedown.widgets import AdminPagedownWidget


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

# Register your models here.
admin.site.register(Article)
