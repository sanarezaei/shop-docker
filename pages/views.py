from django.shortcuts import render
from django.contrib.auth.views import TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'
    
class AboutUsPage(TemplateView):
    template_name= 'pages/aboutus.html'
