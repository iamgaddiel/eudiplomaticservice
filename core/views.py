from django.shortcuts import render
from django.views.generic import TemplateView



class Root(TemplateView):
    template_name = 'core/index.html'


class About(TemplateView):
    template_name = 'core/about.html'


class ContactUs(TemplateView):
    template_name = 'core/contact.html'