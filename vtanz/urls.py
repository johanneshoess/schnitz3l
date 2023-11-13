from django.urls import path
from vtanz.views import IndexView

urlpatterns = [
    path('', IndexView, name='index'),
]
