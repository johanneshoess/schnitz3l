from ..models import Team
from ..forms import TeamForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class TeamFinderView(CreateView):
    """
    Ask Email of User (for identification + matching purpose)
    email there -> load adresses
    no mail -> new adress
    """
    model = Team
    template_name = "jagd/team-finder.html"
    form_class = TeamForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        print('team name is: => ', name)

        # self.object = form.save()

        url = reverse('team', args={name})
        return HttpResponseRedirect(url)
