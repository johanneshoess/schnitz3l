from django.views import generic
from .models import Article
from django.shortcuts import render


def IndexView(request):
    article_list = Article.objects.filter(archived=False)
    pos = 0
    for article in article_list:
        article.pos = 'right' if pos % 2 else 'left'
        pos += 1
    return render(request, 'vtanz/index.html', {'article_list': article_list})


def ArchiveView(request):
    article_list = Article.objects.filter(archived=True)
    pos = 0
    for article in article_list:
        article.pos = 'right' if pos % 2 else 'left'
        pos += 1
    return render(request, 'vtanz/archive.html', {'article_list': article_list})


class DatenschutzView(generic.TemplateView):

    template_name = 'vtanz/datenschutz.html'


class ImpressumView(generic.TemplateView):

    template_name = 'vtanz/impressum.html'


