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
    article_list = Article.objects.all()  # Fetch all articles
    return render(request, 'vtanz/index.html', {'article_list': article_list})



#class IndexView(generic.TemplateView):
    """
    View for information, startpoint
    """
    # article_list

    #template_name = 'vtanz/index.html'


