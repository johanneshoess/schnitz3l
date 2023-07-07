from django.views import generic


class TeamView(generic.TemplateView):
    """
    View for information, startpoint
    """
    template_name = 'jagd/team.html'

    def init(self):
        print('hmmmmmm', self.request)