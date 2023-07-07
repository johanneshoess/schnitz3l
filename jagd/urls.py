from django.urls import path
from jagd.views import IndexView, TeamFinderView, TeamView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('team/', TeamFinderView.as_view(), name="team-finder"),
    path('team/<str:name>', TeamView.as_view(), name="team"),
]
