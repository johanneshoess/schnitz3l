from django.urls import path
from vtanz.views import (
    IndexView,
    DatenschutzView,
    ImpressumView
)

urlpatterns = [
    path('', IndexView, name='index'),
    path('datenschutz', DatenschutzView.as_view(), name='datenschutz'),
    path('impressum', ImpressumView.as_view(), name='impressum')
]
