from django.urls import path
from vtanz.views import (
    IndexView,
    ArchiveView,
    DatenschutzView,
    ImpressumView
)

urlpatterns = [
    path('', IndexView, name='index'),
    path('archive', ArchiveView, name='archive'),
    path('datenschutz', DatenschutzView.as_view(), name='datenschutz'),
    path('impressum', ImpressumView.as_view(), name='impressum')
]
