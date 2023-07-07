from django.urls import path
from n3bu.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]