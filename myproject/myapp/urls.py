from django.urls import path

from .views import homePageView

urlpatterns = [
    url('', homePageView, name='home')
]
