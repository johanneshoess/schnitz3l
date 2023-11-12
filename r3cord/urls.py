from django.urls import path
from r3cord.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
