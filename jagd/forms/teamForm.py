from django import forms
from ..models import Team


class TeamForm(forms.ModelForm):
    """
    Form for creating or find a Team object.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs
        )
        self.fields["name"] = forms.CharField(
            min_length=3,
            empty_value="teamname",
            label="Team Name",
        )

    class Meta:
        model = Team
        fields = ["name"]
