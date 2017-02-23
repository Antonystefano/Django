from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class GraphView(TemplateView):
    template_name = "graph_v02.html"

class SettingsView(TemplateView):
    template_name = "settings_v03.html"

class AboutView(TemplateView):
    template_name = "about.html"

class HelpView(TemplateView):
    template_name = "help.html"