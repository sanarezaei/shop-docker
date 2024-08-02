from django.urls import path
from .views import HomePage, AboutUsPage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('aboutus/', AboutUsPage.as_view(), name='aboutus')
]
