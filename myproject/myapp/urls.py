from django.urls import url

from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
