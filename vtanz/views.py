from django.views import generic
from .models import Article
from django.shortcuts import render


def IndexView(request):
    article = Article(
        headline="Hase ist entlaufen",
        article_id="hase",
        text="Der Hase ist weg, was sollen wir tun? Ich weiß es doch auch nicht. Es ist alles vorbei.",
        image_alt="Ein Hase ist zu sehen"
    )
    #article_list = [article,]
    article_list = Article.objects.all()
    pos = 0
    for article in article_list:
        article.pos = 'right' if pos % 2 else 'left'
        pos += 1
    return render(request, 'vtanz/index.html', {'article_list': article_list})



class DatenschutzView(generic.TemplateView):

    template_name = 'vtanz/datenschutz.html'


class ImpressumView(generic.TemplateView):

    template_name = 'vtanz/impressum.html'


