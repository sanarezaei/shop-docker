from django.contrib import path
from .views import Homepage, AboutUsPage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('aboutus/', AboutUsPage.as_view(), name='aboutus')
]
