from django.views import generic

class IndexView(generic.TemplateView):
    """
    R3cord Startpoint
    """
    template_name = 'r3cord/index.html'
