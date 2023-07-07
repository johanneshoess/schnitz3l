from django.views import generic


class IndexView(generic.TemplateView):
    """
    View for information, startpoint
    """
    template_name = 'n3bu/index.html'
